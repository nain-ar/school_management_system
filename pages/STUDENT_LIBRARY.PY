import streamlit as st
import pandas as pd
from database.database import Database


def show_student_library():

    st.title("📚 My Library")

    db = Database()

    if not db.connect():
        st.error("Database Connection Failed")
        return

    admission_no = st.session_state.username

    # Get student_id
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

    db.execute("""
        SELECT
            l.book_code,
            l.book_name,
            l.author,
            li.issue_date,
            li.return_date,
            li.fine,
            li.status
        FROM library_issues li
        JOIN library l
            ON li.book_id = l.book_id
        WHERE li.student_id = ?
        ORDER BY li.issue_date DESC
    """, (student_id,))

    books = db.fetchall()

    db.close()

    if not books:
        st.info("No books issued.")
        return

    df = pd.DataFrame(
        books,
        columns=[
            "Book Code",
            "Book Name",
            "Author",
            "Issue Date",
            "Return Date",
            "Fine",
            "Status"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    if st.button("⬅ Back", use_container_width=True):
        st.session_state.page = "student_dashboard"
        st.rerun()