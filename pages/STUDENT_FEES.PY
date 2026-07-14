import streamlit as st
import pandas as pd
from database.database import Database


def show_student_fees():

    st.title("💰 My Fees")

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

    # Fetch Fee Records
    db.execute("""
        SELECT
            fee_type,
            amount,
            paid_amount,
            due_amount,
            payment_date,
            status
        FROM fees
        WHERE student_id=?
    """, (student_id,))

    fees = db.fetchall()

    db.close()

    if not fees:
        st.info("No fee records found.")
        return

    df = pd.DataFrame(
        fees,
        columns=[
            "Fee Type",
            "Amount",
            "Paid",
            "Due",
            "Payment Date",
            "Status"
        ]
    )

    total_amount = df["Amount"].sum()
    total_paid = df["Paid"].sum()
    total_due = df["Due"].sum()

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Fee", f"₹ {total_amount:,.0f}")
    c2.metric("Paid", f"₹ {total_paid:,.0f}")
    c3.metric("Due", f"₹ {total_due:,.0f}")

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