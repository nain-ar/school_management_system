import streamlit as st
from modules.auth import Authentication


def show_login():

    auth = Authentication()

    # Create default admin (only once)
    auth.register("admin", "admin123", "Admin")

    st.title(f"🔐 {st.session_state.role} Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Back", use_container_width=True):
            st.session_state.page = "welcome"
            st.rerun()

    with col2:
        if st.button("Login", use_container_width=True):

            if not username or not password:
                st.warning("Please enter username and password.")

            else:
                result = auth.login(
                    username,
                    password,
                    st.session_state.role
                )

                if result["success"]:

                    st.session_state.logged_in = True
                    st.session_state.user_id = result["id"]
                    st.session_state.username = result["username"]
                    st.session_state.role = result["role"]

                    st.session_state.page = "dashboard"
                    st.rerun()

                else:
                    st.error("Invalid Username or Password")