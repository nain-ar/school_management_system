import streamlit as st
from modules.auth import Authentication


def show_login():

    auth = Authentication()

    # Create default admin (only once)
    auth.register("admin", "admin123", "Admin")

    st.title(f"🔐 {st.session_state.role} Login")

    if st.session_state.role == "Student":
        username = st.text_input("Admission Number")

    elif st.session_state.role == "Teacher":
        username = st.text_input("Employee ID")

    elif st.session_state.role == "Parent":
        username = st.text_input("Admission Number")

    else:
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

                 

                    role = result["role"]

                    st.session_state.logged_in = True
                    st.session_state.user_id = result["id"]
                    st.session_state.username = result["username"]
                    st.session_state.role = role
                    
                    if role == "Admin":
                        st.session_state.page = "admin_dashboard"

                    elif role == "Teacher":

                        st.session_state.page = "teacher_dashboard"

                        st.session_state.teacher_id = result["id"]

                        st.session_state.employee_id = result["employee_id"]

                    elif role == "Student":
                        st.session_state.page = "student_dashboard"
                        st.session_state.admission_no = result["admission_no"]

                    elif role == "Parent":
                        st.session_state.page = "parent_dashboard"
                        st.session_state.admission_no = result["admission_no"]

                    st.rerun()

                else:
                    st.error("Invalid Username or Password")