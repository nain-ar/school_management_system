import streamlit as st

def role_card(icon, role):

    st.markdown(
        f"""
        <div style="
            background:white;
            border-radius:18px;
            padding:30px;
            text-align:center;
            box-shadow:0 4px 12px rgba(0,0,0,.15);
            margin-bottom:10px;
        ">
            <div style="font-size:60px;">{icon}</div>
            <h3>{role}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(f"Continue as {role}", key=role, use_container_width=True):
        st.session_state.role = role
        st.session_state.page = "login"
        st.rerun()


def show_welcome():

    st.title("🏫 School Management System")

    st.caption("Choose Your Portal")

    col1, col2 = st.columns(2)

    with col1:
        role_card("🛡️", "Admin")
        role_card("🎓", "Student")

    with col2:
        role_card("👩‍🏫", "Teacher")
        role_card("👨‍👩‍👧", "Parent")