import streamlit as st


def show_parent_dashboard():

    st.title("👨‍👩‍👧 Parent Dashboard")

    st.write(f"Welcome **{st.session_state.username}** 👋")

    st.divider()

    if st.button("👦 Ward Profile", use_container_width=True):
        pass

    if st.button("📅 Attendance", use_container_width=True):
        pass

    if st.button("📝 Results", use_container_width=True):
        pass

    if st.button("💰 Fees", use_container_width=True):
        pass

    st.divider()

    if st.button("Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.session_state.page = "welcome"
        st.rerun()