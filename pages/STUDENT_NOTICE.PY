import streamlit as st
import pandas as pd
from database.database import Database


def show_student_notice():

    st.title("📢 School Notices")

    db = Database()

    if not db.connect():
        st.error("Database Connection Failed")
        return

    db.execute("""
        SELECT
            title,
            description,
            notice_date,
            audience
        FROM notices
        WHERE audience IN ('All','Students')
        ORDER BY notice_date DESC
    """)

    notices = db.fetchall()

    db.close()

    if not notices:
        st.info("No notices available.")
        return

    df = pd.DataFrame(
        notices,
        columns=[
            "Title",
            "Description",
            "Date",
            "Audience"
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