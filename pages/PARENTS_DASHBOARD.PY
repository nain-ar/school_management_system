
import streamlit as st


def show_parent_dashboard():
    if "parent_page" not in st.session_state:
        st.session_state.parent_page = "dashboard"
    st.markdown("""
    <style>

/* Dashboard Cards */
div.stButton > button{
    width:100%;
    height:90px;
    border-radius:15px;
    border:1px solid #E5E7EB;
    background:#FFFFFF;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
    font-size:18px;
    font-weight:600;
    transition:0.25s;
    margin-bottom:12px;
    padding:10px;
}

div.stButton > button:hover{
    transform:translateY(-3px);
    box-shadow:0 8px 18px rgba(0,0,0,0.15);
    border-color:#4CAF50;
    background:#F8FFF8;
}


    </style>
    """, unsafe_allow_html=True)

    st.title("👨‍👩‍👧 Parent Dashboard")
    st.write(f"Welcome **{st.session_state.username}** 👋")
    if st.session_state.parent_page == "ward_profile":

        st.title("👦 Ward Profile")

        st.write("This is the Ward Profile page.")

        if st.button("⬅ Back"):
            st.session_state.parent_page = "dashboard"
            st.rerun()

        return
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👦 Ward Profile", use_container_width=True):
            st.session_state.parent_page = "ward_profile"
            st.rerun()
            
    with col2:
        st.button("📅 Attendance", use_container_width=True)
        
    col3, col4 = st.columns(2)

    with col3:
        st.button("📝 Results", use_container_width=True)
        
    with col4:
        st.button("💰 Fees", use_container_width=True)
        
    st.divider()

    if st.button(" Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.session_state.page = "welcome"
        st.rerun()