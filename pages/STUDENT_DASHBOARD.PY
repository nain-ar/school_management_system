import streamlit as st


# ===============================
# Card
# ===============================
def dashboard_card(title, icon, page):

    st.markdown(
        f"""
        <style>
        .dashboard-card{{
            background:#ffffff;
            border-radius:18px;
            padding:25px;
            text-align:center;
            box-shadow:0 5px 15px rgba(0,0,0,.15);
            transition:0.3s;
            margin-bottom:10px;
        }}

        .dashboard-card:hover{{
            transform:translateY(-8px);
            box-shadow:0 12px 25px rgba(0,0,0,.25);
        }}

        .dashboard-card .icon{{
            font-size:45px;
        }}

        .dashboard-card h3{{
            margin-top:10px;
            margin-bottom:5px;
        }}
        </style>

        <div class="dashboard-card">
            <div class="icon">{icon}</div>
            <h3>{title}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        f"Open {title}",
        key=f"card_{page}",
        use_container_width=True
    ):
        st.session_state.page = page
        st.rerun()


# ===============================
# Dashboard
# ===============================
def show_student_dashboard():

    st.title("🎓 Student Dashboard")

    st.write(f"Welcome **{st.session_state.username}** 👋")

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        dashboard_card("My Profile", "👤", "student_profile")

    with c2:
        dashboard_card("Attendance", "📅", "student_attendance")

    with c3:
        dashboard_card("Results", "📝", "student_results")

    c4, c5, c6 = st.columns(3)

    with c4:
        dashboard_card("Fees", "💰", "student_fees")

    with c5:
        dashboard_card("Library", "📚", "student_library")

    with c6:
        dashboard_card("Notices", "📢", "student_notice")
   

    st.divider()

    if st.button(" Logout", use_container_width=True):

        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.session_state.page = "welcome"

        st.rerun()