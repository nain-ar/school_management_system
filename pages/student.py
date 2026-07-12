import streamlit as st
import pandas as pd
from modules.student import Student


def show_students():

    student = Student()

    st.title("🎓 Student Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Add Student",
        "📋 View Students",
        "🔍 Search",
        "🗑 Delete"
    ])

    # =====================================================
    # ADD STUDENT
    # =====================================================
    with tab1:

        st.subheader("Add Student")

        admission_no = st.text_input("Admission Number")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

        dob = st.date_input("Date of Birth")

        phone = st.text_input("Phone")

        email = st.text_input("Email")

        address = st.text_area("Address")

        col1, col2, col3 = st.columns(3)

        with col1:
            class_name = st.text_input("Class")

        with col2:
            section = st.text_input("Section")

        with col3:
            roll_no = st.text_input("Roll No")

        admission_date = st.date_input("Admission Date")

        photo = st.file_uploader(
            "Student Photo",
            type=["jpg", "jpeg", "png"]
        )

        if st.button("Add Student"):

            student.add_student(
                admission_no,
                first_name,
                last_name,
                gender,
                str(dob),
                phone,
                email,
                address,
                class_name,
                section,
                roll_no,
                str(admission_date)
            )

            st.success("Student Added Successfully!")

    # =====================================================
    # VIEW STUDENTS
    # =====================================================
    with tab2:

        st.subheader("All Students")

        students = student.get_all_students()

        if students:

            columns = [
                "ID",
                "Admission No",
                "First Name",
                "Last Name",
                "Gender",
                "DOB",
                "Phone",
                "Email",
                "Address",
                "Class",
                "Section",
                "Roll No",
                "Admission Date",
                "Photo",
                "QR Code",
                "Status",
                "Created At"
            ]

            df = pd.DataFrame(
                students,
                columns=columns
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        else:
            st.info("No Students Found.")

    # =====================================================
    # SEARCH
    # =====================================================
    with tab3:

        keyword = st.text_input(
            "Search Student"
        )

        if keyword:

            data = student.search_student(
                keyword
            )

            if data:

                columns = [
                    "ID",
                    "Admission No",
                    "First Name",
                    "Last Name",
                    "Gender",
                    "DOB",
                    "Phone",
                    "Email",
                    "Address",
                    "Class",
                    "Section",
                    "Roll No",
                    "Admission Date",
                    "Photo",
                    "QR Code",
                    "Status",
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
                st.warning("Student Not Found.")

    # =====================================================
    # DELETE
    # =====================================================
    with tab4:

        st.subheader("Delete Student")

        student_id = st.number_input(
            "Student ID",
            min_value=1,
            step=1
        )

        if st.button("Delete Student"):

            student.delete_student(
                student_id
            )

            st.success("Student Deleted Successfully!")