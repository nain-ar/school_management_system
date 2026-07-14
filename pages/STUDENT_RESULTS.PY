import streamlit as st
import pandas as pd
from database.database import Database


def show_student_results():

    st.title("📝 My Results")

    db = Database()

    if not db.connect():
        st.error("Database Connection Failed")
        return

    admission_no = st.session_state.username

    # Get student ID
    db.execute("""
        SELECT student_id
        FROM students
        WHERE admission_no=?
    """, (admission_no,))

    student = db.fetchone()

    if student is None:
        st.error("Student not found.")
        db.close()
        return

    student_id = student[0]

    # Fetch Results
    db.execute("""
        SELECT
            exams.exam_name,
            subjects.subject_name,
            results.marks_obtained,
            exams.total_marks,
            results.grade,
            results.remarks
        FROM results
        JOIN exams
            ON results.exam_id = exams.exam_id
        JOIN subjects
            ON exams.subject_id = subjects.subject_id
        WHERE results.student_id=?
    """, (student_id,))

    data = db.fetchall()

    db.close()

    if not data:
        st.info("No results available.")
        return

    df = pd.DataFrame(
        data,
        columns=[
            "Exam",
            "Subject",
            "Marks",
            "Total",
            "Grade",
            "Remarks"
        ]
    )

    total_marks = df["Marks"].sum()
    total_possible = df["Total"].sum()

    percentage = (
        (total_marks / total_possible) * 100
        if total_possible else 0
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Subjects", len(df))
    c2.metric("Total Marks", f"{total_marks}/{total_possible}")
    c3.metric("Percentage", f"{percentage:.2f}%")

    st.divider()

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    if st.button("⬅ Back", use_container_width=True):
        st.session_state.page = "student_dashboard"
        st.rerun()