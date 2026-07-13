import streamlit as st
from pages.dashboard import show_dashboard
from pages.welcome import show_welcome
from pages.login import show_login
from database.db import create_tables
from pages.student import show_students
from pages.teachers import show_teachers
from pages.parents import show_parents
from pages.fees import show_fees 
from pages.attendence import show_attendance
from pages.exams  import show_exams
from pages.studentid import show_id_card
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
elif st.session_state.page == "teachers":
    show_teachers()

elif st.session_state.page == "parents":
    show_parents()
elif st.session_state.page == "fees":
    show_fees()
elif st.session_state.page == "attendence":
    show_attendance()
elif st.session_state.page == "exams":
    show_exams()
elif st.session_state.page == "id_card":
    show_id_card()
def load_css():

    with open("assets/css/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()