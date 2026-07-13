import streamlit as st
import pandas as pd
from modules.parent import Parent


def show_parents():

    parent = Parent()
   
    st.title("👨‍👩‍👧 Parent Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Add Parent",
        "📋 View Parents",
        "🔍 Search",
        "🗑 Delete"
    ])

    # =====================================================
    # ADD PARENT
    # =====================================================
    with tab1:

        st.subheader("Add Parent")

        student_id = st.number_input(
            "Student ID",
            min_value=1,
            step=1
        )

        father_name = st.text_input("Father Name")

        mother_name = st.text_input("Mother Name")

        phone = st.text_input("Phone Number")

        email = st.text_input("Email")

        address = st.text_area("Address")

        if st.button("Add Parent"):

            parent.add_parent(
                student_id,
                father_name,
                mother_name,
                phone,
                email,
                address
            )

            st.success("Parent Added Successfully!")

    # =====================================================
    # VIEW PARENTS
    # =====================================================
    with tab2:

        st.subheader("All Parents")

        data = parent.get_all_parents()

        if data:

            columns = [
                "Parent ID",
                "Student ID",
                "Father Name",
                "Mother Name",
                "Phone",
                "Email",
                "Address"
            ]

            df = pd.DataFrame(
                data,
                columns=columns
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        else:
            st.info("No Parent Records Found.")

    # =====================================================
    # SEARCH PARENT
    # =====================================================
    with tab3:

        st.subheader("Search Parent")

        keyword = st.text_input(
            "Search by Father Name, Mother Name, Phone or Email"
        )

        if keyword:

            data = parent.search_parent(keyword)

            if data:

                columns = [
                    "Parent ID",
                    "Student ID",
                    "Father Name",
                    "Mother Name",
                    "Phone",
                    "Email",
                    "Address"
                ]

                df = pd.DataFrame(
                    data,
                    columns=columns
                )

                st.dataframe(
                    df,
                    use_container_width=True
                )

            else:
                st.warning("Parent Not Found.")

    # =====================================================
    # DELETE PARENT
    # =====================================================
    with tab4:

        st.subheader("Delete Parent")

        parent_id = st.number_input(
            "Parent ID",
            min_value=1,
            step=1
        )

        confirm = st.checkbox(
            "I confirm that I want to delete this parent."
        )

        if st.button("Delete Parent"):

            if confirm:

                parent.delete_parent(parent_id)

                st.success("Parent Deleted Successfully!")

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