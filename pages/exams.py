import streamlit as st
import pandas as pd
from modules.exam import Exam


def show_exams():

    exam = Exam()
    
    st.title("📝 Exam Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Add Exam",
        "📋 View Exams",
        "🔍 Search",
        "🗑 Delete"
    ])

    # ======================================
    # ADD EXAM
    # ======================================
    with tab1:

        exam_name = st.text_input("Exam Name")

        class_name = st.text_input("Class")

        subject_id = st.number_input(
            "Subject ID",
            min_value=1,
            step=1
        )

        exam_date = st.date_input("Exam Date")

        total_marks = st.number_input(
            "Total Marks",
            min_value=1,
            value=100
        )

        passing_marks = st.number_input(
            "Passing Marks",
            min_value=1,
            value=33
        )

        if st.button("Add Exam"):

            exam.add_exam(
                exam_name,
                class_name,
                subject_id,
                str(exam_date),
                total_marks,
                passing_marks
            )

            st.success("Exam Added Successfully!")

    # ======================================
    # VIEW EXAMS
    # ======================================
    with tab2:

        data = exam.get_all_exams()

        if data:

            columns = [
                "Exam ID",
                "Exam Name",
                "Class",
                "Subject ID",
                "Exam Date",
                "Total Marks",
                "Passing Marks"
            ]

            st.dataframe(
                pd.DataFrame(
                    data,
                    columns=columns
                ),
                use_container_width=True
            )

        else:
            st.info("No Exams Found.")

    # ======================================
    # SEARCH
    # ======================================
    with tab3:

        keyword = st.text_input("Search Exam")

        if keyword:

            data = exam.search_exam(keyword)

            if data:

                columns = [
                    "Exam ID",
                    "Exam Name",
                    "Class",
                    "Subject ID",
                    "Exam Date",
                    "Total Marks",
                    "Passing Marks"
                ]

                st.dataframe(
                    pd.DataFrame(
                        data,
                        columns=columns
                    ),
                    use_container_width=True
                )

            else:
                st.warning("Exam Not Found.")

    # ======================================
    # DELETE
    # ======================================
    with tab4:

        exam_id = st.number_input(
            "Exam ID",
            min_value=1,
            step=1
        )

        confirm = st.checkbox(
            "I confirm that I want to delete this exam."
        )

        if st.button("Delete Exam"):

            if confirm:
                exam.delete_exam(exam_id)
                st.success("Exam Deleted Successfully!")
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