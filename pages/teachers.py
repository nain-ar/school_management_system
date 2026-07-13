import streamlit as st
import pandas as pd
from modules.teacher import Teacher


def show_teachers():

    teacher = Teacher()
   
    st.title("👩‍🏫 Teacher Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Add Teacher",
        "📋 View Teachers",
        "🔍 Search",
        "🗑 Delete"
    ])

    # =====================================
    # ADD TEACHER
    # =====================================
    with tab1:

        st.subheader("Add Teacher")

        employee_id = st.text_input("Employee ID")

        first_name = st.text_input("First Name")

        last_name = st.text_input("Last Name")

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

        dob = st.date_input("Date of Birth")

        phone = st.text_input("Phone Number")

        email = st.text_input("Email")

        address = st.text_area("Address")

        qualification = st.text_input("Qualification")

        department = st.text_input("Department")

        designation = st.text_input("Designation")

        joining_date = st.date_input("Joining Date")

        salary = st.number_input(
            "Salary",
            min_value=0.0,
            step=1000.0
        )

        photo = st.file_uploader(
            "Teacher Photo",
            type=["jpg", "jpeg", "png"]
        )

        if st.button("Add Teacher"):

            teacher.add_teacher(
                employee_id,
                first_name,
                last_name,
                gender,
                str(dob),
                phone,
                email,
                address,
                qualification,
                department,
                designation,
                str(joining_date),
                salary
            )

            st.success("Teacher Added Successfully!")

    # =====================================
    # VIEW TEACHERS
    # =====================================
    with tab2:

        st.subheader("All Teachers")

        data = teacher.get_all_teachers()

        if data:

            columns = [
                "ID",
                "Employee ID",
                "First Name",
                "Last Name",
                "Gender",
                "DOB",
                "Phone",
                "Email",
                "Address",
                "Qualification",
                "Department",
                "Designation",
                "Joining Date",
                "Salary",
                "Photo",
                "Status",
                "Created At"
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
            st.info("No Teachers Found.")

    # =====================================
    # SEARCH TEACHER
    # =====================================
    with tab3:

        st.subheader("Search Teacher")

        keyword = st.text_input("Enter Name or Employee ID")

        if keyword:

            data = teacher.search_teacher(keyword)

            if data:

                columns = [
                    "ID",
                    "Employee ID",
                    "First Name",
                    "Last Name",
                    "Gender",
                    "DOB",
                    "Phone",
                    "Email",
                    "Address",
                    "Qualification",
                    "Department",
                    "Designation",
                    "Joining Date",
                    "Salary",
                    "Photo",
                    "Status",
                    "Created At"
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
                st.warning("Teacher Not Found.")

    # =====================================
    # DELETE TEACHER
    # =====================================
    with tab4:

        st.subheader("Delete Teacher")

        teacher_id = st.number_input(
            "Teacher ID",
            min_value=1,
            step=1
        )

        confirm = st.checkbox(
            "I confirm that I want to delete this teacher."
        )

        if st.button("Delete Teacher"):

            if confirm:
                teacher.delete_teacher(teacher_id)
                st.success("Teacher Deleted Successfully!")

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