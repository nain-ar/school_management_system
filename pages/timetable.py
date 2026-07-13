import streamlit as st
import pandas as pd
from modules.timetable import Timetable


def show_timetable():

    timetable = Timetable()

    st.title("📅 Timetable Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Add Timetable",
        "📋 View Timetable",
        "🔍 Search",
        "🗑 Delete"
    ])

    # =====================================
    # ADD
    # =====================================
    with tab1:

        class_name = st.text_input("Class")

        section = st.text_input("Section")

        subject_id = st.number_input(
            "Subject ID",
            min_value=1,
            step=1
        )

        teacher_id = st.number_input(
            "Teacher ID",
            min_value=1,
            step=1
        )

        day = st.selectbox(
            "Day",
            [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday"
            ]
        )

        start_time = st.text_input(
            "Start Time (09:00)"
        )

        end_time = st.text_input(
            "End Time (10:00)"
        )

        if st.button("Add Timetable"):

            timetable.add_timetable(
                class_name,
                section,
                subject_id,
                teacher_id,
                day,
                start_time,
                end_time
            )

            st.success("Timetable Added Successfully!")

    # =====================================
    # VIEW
    # =====================================
    with tab2:

        data = timetable.get_all_timetable()

        if data:

            columns = [
                "ID",
                "Class",
                "Section",
                "Subject ID",
                "Teacher ID",
                "Day",
                "Start Time",
                "End Time"
            ]

            st.dataframe(
                pd.DataFrame(
                    data,
                    columns=columns
                ),
                use_container_width=True
            )

        else:
            st.info("No Timetable Found.")

    # =====================================
    # SEARCH
    # =====================================
    with tab3:

        keyword = st.text_input(
            "Search Timetable"
        )

        if keyword:

            data = timetable.search_timetable(
                keyword
            )

            if data:

                columns = [
                    "ID",
                    "Class",
                    "Section",
                    "Subject ID",
                    "Teacher ID",
                    "Day",
                    "Start Time",
                    "End Time"
                ]

                st.dataframe(
                    pd.DataFrame(
                        data,
                        columns=columns
                    ),
                    use_container_width=True
                )

            else:
                st.warning("No Record Found.")

    # =====================================
    # DELETE
    # =====================================
    with tab4:

        timetable_id = st.number_input(
            "Timetable ID",
            min_value=1,
            step=1
        )

        if st.button("Delete Timetable"):

            timetable.delete_timetable(
                timetable_id
            )

            st.success(
                "Timetable Deleted Successfully!"
            )

    # =====================================
    # BACK
    # =====================================

    st.divider()

    _, col, _ = st.columns([1, 2, 1])

    with col:
        if st.button(
            "⬅ Back to Dashboard",
            use_container_width=True
        ):
            st.session_state.page = "dashboard"
            st.rerun()