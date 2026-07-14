import streamlit as st
from pages.STUDENT_DASHBOARD import show_student_dashboard
from pages.TEACHER_DASHBOARD import show_teacher_dashboard
from pages.PARENTS_DASHBOARD import show_parent_dashboard
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
from pages.library import show_library
from pages.notice import show_notices
from pages.subject import show_subjects
from pages.STUDENT_PROFILE import show_student_profile
from pages.STUDENT_ATTENDANCE import show_student_attendance
from pages.STUDENT_RESULTS import show_student_results
from pages.STUDENT_FEES import show_student_fees
from pages.STUDENT_LIBRARY import show_student_library
from pages.STUDENT_NOTICE import show_student_notice
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
elif st.session_state.page == "admin_dashboard":
    show_dashboard()

elif st.session_state.page == "student_dashboard":
    show_student_dashboard()
elif st.session_state.page == "student_profile":
    show_student_profile()

elif st.session_state.page == "student_attendance":
    show_student_attendance()

elif st.session_state.page == "student_results":
    show_student_results()

elif st.session_state.page == "student_fees":
    show_student_fees()

elif st.session_state.page == "student_library":
    show_student_library()

elif st.session_state.page == "student_notice":
    show_student_notice()

elif st.session_state.page == "teacher_dashboard":
    show_teacher_dashboard()

elif st.session_state.page == "parent_dashboard":
    show_parent_dashboard()

elif st.session_state.page == "students":
    show_students()
elif st.session_state.page == "students":
    show_students()
elif st.session_state.page == "teachers":
    show_teachers()

elif st.session_state.page == "parents":
    show_parents()
elif st.session_state.page == "fees":
    show_fees()
elif st.session_state.page == "attendance":
    show_attendance()
elif st.session_state.page == "exams":
    show_exams()
elif st.session_state.page == "id_card":
    show_id_card()
elif st.session_state.page == "library":
    show_library()
elif st.session_state.page == "notice":
    show_notices()
elif st.session_state.page == "subject":
    show_subjects()
def load_css():

    with open("assets/css/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()