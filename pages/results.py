import streamlit as st
import pandas as pd
from modules.result import Result


def calculate_grade(marks):

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def show_results():

    result = Result()

    st.title("📊 Result Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Add Result",
        "📋 View Results",
        "🔍 Search",
        "🗑 Delete"
    ])

    # =====================================
    # ADD RESULT
    # =====================================
    with tab1:

        student_id = st.number_input(
            "Student ID",
            min_value=1,
            step=1
        )

        exam_id = st.number_input(
            "Exam ID",
            min_value=1,
            step=1
        )

        marks = st.number_input(
            "Marks Obtained",
            min_value=0.0,
            max_value=100.0
        )

        grade = calculate_grade(marks)

        st.info(f"Grade : {grade}")

        remarks = st.text_area("Remarks")

        if st.button("Add Result"):

            result.add_result(
                student_id,
                exam_id,
                marks,
                grade,
                remarks
            )

            st.success("Result Added Successfully!")

    # =====================================
    # VIEW RESULTS
    # =====================================
    with tab2:

        data = result.get_all_results()

        if data:

            columns = [
                "Result ID",
                "Student ID",
                "Exam ID",
                "Marks",
                "Grade",
                "Remarks"
            ]

            st.dataframe(
                pd.DataFrame(
                    data,
                    columns=columns
                ),
                use_container_width=True
            )

        else:
            st.info("No Results Found.")

    # =====================================
    # SEARCH
    # =====================================
    with tab3:

        keyword = st.text_input("Search Result")

        if keyword:

            data = result.search_result(keyword)

            if data:

                columns = [
                    "Result ID",
                    "Student ID",
                    "Exam ID",
                    "Marks",
                    "Grade",
                    "Remarks"
                ]

                st.dataframe(
                    pd.DataFrame(
                        data,
                        columns=columns
                    ),
                    use_container_width=True
                )

            else:
                st.warning("Result Not Found.")

    # =====================================
    # DELETE
    # =====================================
    with tab4:

        result_id = st.number_input(
            "Result ID",
            min_value=1,
            step=1
        )

        confirm = st.checkbox(
            "I confirm that I want to delete this result."
        )

        if st.button("Delete Result"):

            if confirm:
                result.delete_result(result_id)
                st.success("Result Deleted Successfully!")
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