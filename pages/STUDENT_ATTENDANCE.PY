import streamlit as st
import pandas as pd
from database.database import Database


def show_student_attendance():

    st.title("📅 My Attendance")

    db = Database()

    if not db.connect():
        st.error("Database Connection Failed")
        return

    admission_no = st.session_state.username

    # Get student_id
    db.execute("""
        SELECT student_id, first_name, last_name
        FROM students
        WHERE admission_no=?
    """, (admission_no,))

    student = db.fetchone()

    if student is None:
        st.error("Student not found.")
        db.close()
        return

    student_id = student[0]

    # Attendance
    db.execute("""
        SELECT attendance_date, status, remarks
        FROM attendance
        WHERE student_id=?
        ORDER BY attendance_date DESC
    """, (student_id,))

    attendance = db.fetchall()

    db.close()

    if not attendance:
        st.info("No attendance records found.")
    else:

        df = pd.DataFrame(
            attendance,
            columns=[
                "Date",
                "Status",
                "Remarks"
            ]
        )

        total = len(df)
        present = len(df[df["Status"] == "Present"])
        absent = len(df[df["Status"] == "Absent"])
        late = len(df[df["Status"] == "Late"])

        percentage = (present / total) * 100 if total else 0

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Present", present)
        c2.metric("Absent", absent)
        c3.metric("Late", late)
        c4.metric("Attendance %", f"{percentage:.1f}%")

        st.divider()

        st.dataframe(
            df,
            use_container_width=True
        )

    st.divider()

    if st.button("⬅ Back", use_container_width=True):
        st.session_state.page = "student_dashboard"
        st.rerun()