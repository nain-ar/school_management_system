import streamlit as st
from pages.dashboard import show_dashboard
from pages.welcome import show_welcome
from pages.login import show_login
from database.db import create_tables
from pages.student import show_students

create_tables()
st.set_page_config(
    page_title="School Management System",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Hide Streamlit default UI
st.markdown("""
<style>

/* Hide Sidebar */
[data-testid="stSidebar"]{
    display:none;
}

/* Hide collapsed sidebar button */
[data-testid="collapsedControl"]{
    display:none;
}

/* Hide Header */
header{
    visibility:hidden;
}

/* Hide Footer */
footer{
    visibility:hidden;
}

/* Remove top padding */
.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Session State ---------------- #

import streamlit as st

# ---------------- Session State ----------------

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "role" not in st.session_state:
    st.session_state.role = ""

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------------- Navigation ---------------- #

if st.session_state.page == "welcome":
    show_welcome()

elif st.session_state.page == "login":
    show_login()

elif st.session_state.page == "dashboard":
    show_dashboard()
elif st.session_state.page == "students":
    show_students()

def load_css():

    with open("assets/css/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()