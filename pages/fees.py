import streamlit as st
import pandas as pd
from modules.fees import Fees


def show_fees():

    fee = Fees()
  
    st.title("💰 Fee Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Add Fee",
        "📋 View Fees",
        "🔍 Search",
        "🗑 Delete"
    ])

    # ======================================
    # ADD FEE
    # ======================================
    with tab1:

        student_id = st.number_input(
            "Student ID",
            min_value=1,
            step=1
        )

        fee_type = st.selectbox(
            "Fee Type",
            [
                "Tuition",
                "Transport",
                "Library",
                "Hostel",
                "Exam",
                "Other"
            ]
        )

        amount = st.number_input(
            "Total Amount",
            min_value=0.0
        )

        paid_amount = st.number_input(
            "Paid Amount",
            min_value=0.0
        )

        due_amount = amount - paid_amount

        st.info(f"Due Amount: ₹{due_amount:.2f}")

        payment_date = st.date_input(
            "Payment Date"
        )

        status = st.selectbox(
            "Status",
            ["Paid", "Partial", "Pending"]
        )

        if st.button("Add Fee"):

            fee.add_fee(
                student_id,
                fee_type,
                amount,
                paid_amount,
                due_amount,
                str(payment_date),
                status
            )

            st.success("Fee Record Added Successfully!")

    # ======================================
    # VIEW FEES
    # ======================================
    with tab2:

        data = fee.get_all_fees()

        if data:

            columns = [
                "Fee ID",
                "Student ID",
                "Fee Type",
                "Amount",
                "Paid",
                "Due",
                "Payment Date",
                "Status"
            ]

            st.dataframe(
                pd.DataFrame(
                    data,
                    columns=columns
                ),
                use_container_width=True
            )

        else:
            st.info("No Fee Records Found.")

    # ======================================
    # SEARCH
    # ======================================
    with tab3:

        keyword = st.text_input("Search Fee")

        if keyword:

            data = fee.search_fee(keyword)

            if data:

                columns = [
                    "Fee ID",
                    "Student ID",
                    "Fee Type",
                    "Amount",
                    "Paid",
                    "Due",
                    "Payment Date",
                    "Status"
                ]

                st.dataframe(
                    pd.DataFrame(
                        data,
                        columns=columns
                    ),
                    use_container_width=True
                )

            else:
                st.warning("No Fee Record Found.")

    # ======================================
    # DELETE
    # ======================================
    with tab4:

        fee_id = st.number_input(
            "Fee ID",
            min_value=1,
            step=1
        )

        confirm = st.checkbox(
            "I confirm that I want to delete this fee record."
        )

        if st.button("Delete Fee"):

            if confirm:
                fee.delete_fee(fee_id)
                st.success("Fee Deleted Successfully!")
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