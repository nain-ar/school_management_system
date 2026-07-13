import streamlit as st
import pandas as pd
from modules.subject import Subject


def show_subjects():

    subject = Subject()
 
    st.title("📚 Subject Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Add Subject",
        "📋 View Subjects",
        "🔍 Search",
        "🗑 Delete"
    ])

    # ======================================
    # ADD SUBJECT
    # ======================================
    with tab1:

        st.subheader("Add Subject")

        subject_code = st.text_input("Subject Code")

        subject_name = st.text_input("Subject Name")

        class_name = st.text_input("Class")

        teacher_id = st.number_input(
            "Teacher ID",
            min_value=1,
            step=1
        )

        credits = st.number_input(
            "Credits",
            min_value=1,
            value=1
        )

        if st.button("Add Subject"):

            subject.add_subject(
                subject_code,
                subject_name,
                class_name,
                teacher_id,
                credits
            )

            st.success("Subject Added Successfully!")

    # ======================================
    # VIEW SUBJECTS
    # ======================================
    with tab2:

        st.subheader("All Subjects")

        data = subject.get_all_subjects()

        if data:

            columns = [
                "ID",
                "Subject Code",
                "Subject Name",
                "Class",
                "Teacher ID",
                "Credits",
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
            st.info("No Subjects Found.")

    # ======================================
    # SEARCH
    # ======================================
    with tab3:

        keyword = st.text_input("Search Subject")

        if keyword:

            data = subject.search_subject(keyword)

            if data:

                columns = [
                    "ID",
                    "Subject Code",
                    "Subject Name",
                    "Class",
                    "Teacher ID",
                    "Credits",
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
                st.warning("Subject Not Found.")

    # ======================================
    # DELETE
    # ======================================
    with tab4:

        subject_id = st.number_input(
            "Subject ID",
            min_value=1,
            step=1
        )

        confirm = st.checkbox(
            "I confirm that I want to delete this subject."
        )

        if st.button("Delete Subject"):

            if confirm:
                subject.delete_subject(subject_id)
                st.success("Subject Deleted Successfully!")
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