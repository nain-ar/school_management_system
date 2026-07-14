import streamlit as st
from database.database import Database


def show_student_profile():

    st.title("👤 My Profile")

    db = Database()

    if not db.connect():
        st.error("Database Connection Failed")
        return

    # Logged-in student's admission number
    admission_no = st.session_state.username

    db.execute("""
        SELECT
            admission_no,
            first_name,
            last_name,
            gender,
            dob,
            phone,
            email,
            address,
            class_name,
            section,
            roll_no,
            admission_date,
            photo
        FROM students
        WHERE admission_no = ?
    """, (admission_no,))

    student = db.fetchone()

    db.close()

    if not student:
        st.error("Student not found.")
        return

    col1, col2 = st.columns([1, 3])

    with col1:

        if student[12]:
            st.image(student[12], width=180)
        else:
            st.image(
                "https://via.placeholder.com/180",
                width=180
            )

    with col2:

        st.subheader(f"{student[1]} {student[2]}")

        st.write(f"**Admission No:** {student[0]}")
        st.write(f"**Gender:** {student[3]}")
        st.write(f"**Date of Birth:** {student[4]}")
        st.write(f"**Phone:** {student[5]}")
        st.write(f"**Email:** {student[6]}")
        st.write(f"**Address:** {student[7]}")
        st.write(f"**Class:** {student[8]}-{student[9]}")
        st.write(f"**Roll No:** {student[10]}")
        st.write(f"**Admission Date:** {student[11]}")

    st.divider()

    if st.button("⬅ Back"):
        st.session_state.page = "student_dashboard"
        st.rerun()