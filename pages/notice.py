import streamlit as st
import pandas as pd
from modules.notice import Notice


def show_notices():

    notice = Notice()

    st.title("📢 Notice Board")

    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Add Notice",
        "📋 View Notices",
        "🔍 Search",
        "🗑 Delete"
    ])

    # =====================================
    # ADD NOTICE
    # =====================================
    with tab1:

        title = st.text_input("Notice Title")

        description = st.text_area("Description")

        notice_date = st.date_input("Notice Date")

        audience = st.selectbox(
            "Audience",
            [
                "All",
                "Students",
                "Teachers",
                "Parents"
            ]
        )

        if st.button("Publish Notice"):

            notice.add_notice(
                title,
                description,
                str(notice_date),
                audience
            )

            st.success("Notice Published Successfully!")

    # =====================================
    # VIEW
    # =====================================
    with tab2:

        data = notice.get_all_notices()

        if data:

            columns = [
                "Notice ID",
                "Title",
                "Description",
                "Notice Date",
                "Audience",
                "Created At"
            ]

            st.dataframe(
                pd.DataFrame(
                    data,
                    columns=columns
                ),
                use_container_width=True
            )

        else:
            st.info("No Notices Found.")

    # =====================================
    # SEARCH
    # =====================================
    with tab3:

        keyword = st.text_input("Search Notice")

        if keyword:

            data = notice.search_notice(keyword)

            if data:

                columns = [
                    "Notice ID",
                    "Title",
                    "Description",
                    "Notice Date",
                    "Audience",
                    "Created At"
                ]

                st.dataframe(
                    pd.DataFrame(
                        data,
                        columns=columns
                    ),
                    use_container_width=True
                )

            else:
                st.warning("Notice Not Found.")

    # =====================================
    # DELETE
    # =====================================
    with tab4:

        notice_id = st.number_input(
            "Notice ID",
            min_value=1,
            step=1
        )

        if st.button("Delete Notice"):

            notice.delete_notice(notice_id)

            st.success("Notice Deleted Successfully!")

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