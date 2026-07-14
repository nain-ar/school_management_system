import streamlit as st


def show_teacher_dashboard():

    st.title("👩‍🏫 Teacher Dashboard")

    st.write(f"Welcome **{st.session_state.username}** 👋")

    st.divider()

    if st.button("🎓 Students", use_container_width=True):
        pass

    if st.button("📅 Attendance", use_container_width=True):
        pass

    if st.button("📝 Exams", use_container_width=True):
        pass

    if st.button("📢 Notices", use_container_width=True):
        pass

    st.divider()

    if st.button("Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.session_state.page = "welcome"
        st.rerun()