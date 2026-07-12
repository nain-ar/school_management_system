import streamlit as st
from database.database import Database


# ===============================
# Statistic Card
# ===============================
def stat_card(title, value, icon):

#     st.markdown(f"""
#     <div class="stat-card">

#         <div class="icon">
#             {icon}
#         </div>

#         <h2>{value}</h2>

#         <p>{title}</p>

#     </div>
#     """, unsafe_allow_html=True)
    st.markdown(
f"""
<div class="stat-card">
    <div class="icon">{icon}</div>
    <h2>{value}</h2>
    <p>{title}</p>
</div>
""",
unsafe_allow_html=True
)


# ===============================
# Module Card
# ===============================
def module_card(title, icon, page=None):

    # st.markdown(f"""
    # <div class="module-card">

    #     <div class="module-icon">
    #         {icon}
    #     </div>

    #     <h3>{title}</h3>

    # </div>
    # """, unsafe_allow_html=True)
    st.markdown(
f"""
<div class="module-card">
    <div class="module-icon">{icon}</div>
    <h3>{title}</h3>
</div>
""",
unsafe_allow_html=True
)

    if page:

        if st.button(
            "Open",
            key=page,
            use_container_width=True
        ):

            st.session_state.page = page
            st.rerun()



# ===============================
# Count From Database
# ===============================
def get_count(table_name):

    db = Database()

    if db.connect():

        db.execute(
            f"SELECT COUNT(*) FROM {table_name}"
        )

        result = db.fetchone()

        db.close()

        return result[0]

    return 0



# ===============================
# Dashboard
# ===============================
def show_dashboard():


    # CSS
    st.markdown("""
    <style>


    .stat-card{

        background:white;
        border-radius:15px;
        padding:20px;
        text-align:center;
        box-shadow:0 5px 15px rgba(0,0,0,0.15);
        margin-bottom:20px;

    }


    .stat-card .icon{

        font-size:35px;

    }



    .module-card{

        background:white;
        border-radius:18px;
        height:130px;
        text-align:center;
        padding-top:25px;
        box-shadow:0 5px 15px rgba(0,0,0,0.15);
        transition:0.3s;

    }


    .module-card:hover{

        transform:translateY(-5px);
        box-shadow:0 10px 25px rgba(0,0,0,0.25);

    }


    .module-icon{

        font-size:40px;

    }


    .stButton button{
    border-radius:15px;
    height:35px;
}


    </style>
    """, unsafe_allow_html=True)



    students = get_count("students")
    teachers = get_count("teachers")
    parents = get_count("parents")



    st.title("🏫 Admin Dashboard")


    st.write(
        f"Welcome **{st.session_state.username}** 👋"
    )


    st.divider()



    st.subheader("Dashboard Overview")


    c1,c2,c3,c4 = st.columns(4)


    with c1:
        stat_card(
            "Students",
            students,
            "🎓"
        )


    with c2:
        stat_card(
            "Teachers",
            teachers,
            "👩‍🏫"
        )


    with c3:
        stat_card(
            "Parents",
            parents,
            "👨‍👩‍👧"
        )


    with c4:
        stat_card(
            "Classes",
            12,
            "🏫"
        )



    st.divider()


    st.subheader("Quick Access")



    r1c1,r1c2,r1c3,r1c4 = st.columns(4)


    with r1c1:
        module_card(
            "Students",
            "🎓",
            "students"
        )


    with r1c2:
        module_card(
            "Teachers",
            "👩‍🏫",
            "teachers"
        )


    with r1c3:
        module_card(
            "Parents",
            "👨‍👩‍👧",
            "parents"
        )


    with r1c4:
        module_card(
            "Attendance",
            "📅",
            "attendance"
        )



    r2c1,r2c2,r2c3,r2c4 = st.columns(4)


    with r2c1:
        module_card(
            "Fees",
            "💰",
            "fees"
        )


    with r2c2:
        module_card(
            "Exams",
            "📝",
            "exams"
        )


    with r2c3:
        module_card(
            "Library",
            "📚",
            "library"
        )


    with r2c4:
        module_card(
            "Reports",
            "📊",
            "reports"
        )



    st.divider()



    if st.button(
        " Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.session_state.page = "welcome"

        st.rerun()