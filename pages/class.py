import streamlit as st
import pandas as pd
from modules.class_mg import ClassManagement


def show_classes():

    classroom = ClassManagement()
   
    st.title("🏫 Class Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Add Class",
        "📋 View Classes",
        "🔍 Search",
        "🗑 Delete"
    ])

    # =====================================
    # ADD CLASS
    # =====================================
    with tab1:

        st.subheader("Add Class")

        class_name = st.text_input("Class Name")

        section = st.text_input("Section")

        class_teacher = st.number_input(
            "Class Teacher ID",
            min_value=1,
            step=1
        )

        room_number = st.text_input("Room Number")

        capacity = st.number_input(
            "Capacity",
            min_value=1,
            step=1
        )

        if st.button("Add Class"):

            classroom.add_class(
                class_name,
                section,
                class_teacher,
                room_number,
                capacity
            )

            st.success("Class Added Successfully!")

    # =====================================
    # VIEW CLASSES
    # =====================================
    with tab2:

        data = classroom.get_all_classes()

        if data:

            columns = [
                "ID",
                "Class",
                "Section",
                "Teacher ID",
                "Room Number",
                "Capacity",
                "Created At"
            ]

            st.dataframe(
                pd.DataFrame(
                    data,
                    columns=columns
                ),
                use_container_width=True
            )

        else:
            st.info("No Classes Found.")

    # =====================================
    # SEARCH CLASS
    # =====================================
    with tab3:

        keyword = st.text_input("Search Class")

        if keyword:

            data = classroom.search_class(keyword)

            if data:

                columns = [
                    "ID",
                    "Class",
                    "Section",
                    "Teacher ID",
                    "Room Number",
                    "Capacity",
                    "Created At"
                ]

                st.dataframe(
                    pd.DataFrame(
                        data,
                        columns=columns
                    ),
                    use_container_width=True
                )

            else:
                st.warning("Class Not Found.")

    # =====================================
    # DELETE CLASS
    # =====================================
    with tab4:

        class_id = st.number_input(
            "Class ID",
            min_value=1,
            step=1
        )

        confirm = st.checkbox(
            "I confirm that I want to delete this class."
        )

        if st.button("Delete Class"):

            if confirm:
                classroom.delete_class(class_id)
                st.success("Class Deleted Successfully!")
            else:
                st.warning("Please confirm before deleting.")
        
    st.divider()

    _, col, _ = st.columns([1, 2, 1])

    with col:
        if st.button(
            "⬅ Back to Dashboard",
            use_container_width=True
        ):
            st.session_state.page = "dashboard"
            st.rerun()