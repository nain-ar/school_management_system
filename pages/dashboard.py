import streamlit as st

def stat_card(title, value, icon):
    st.markdown(f"""
    <div style="
        background:white;
        border-radius:15px;
        padding:20px;
        text-align:center;
        box-shadow:0 5px 15px rgba(0,0,0,0.15);
        margin-bottom:20px;
    ">
        <div style="font-size:35px;">{icon}</div>
        <h2 style="margin:5px 0;">{value}</h2>
        <p style="color:gray;">{title}</p>
    </div>
    """, unsafe_allow_html=True)


def module_card(title, icon):
    st.markdown(f"""
    <div style="
        background:white;
        border-radius:15px;
        padding:30px;
        text-align:center;
        box-shadow:0 5px 15px rgba(0,0,0,.15);
        margin-bottom:20px;
        cursor:pointer;
    ">
        <div style="font-size:40px;">{icon}</div>
        <h3>{title}</h3>
    </div>
    """, unsafe_allow_html=True)


def show_dashboard():

    st.title("🏫 Admin Dashboard")

    st.write(f"Welcome **{st.session_state.username}** 👋")

    st.divider()

    st.subheader("Dashboard Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        stat_card("Students", "250", "🎓")

    with c2:
        stat_card("Teachers", "25", "👩‍🏫")

    with c3:
        stat_card("Parents", "220", "👨‍👩‍👧")

    with c4:
        stat_card("Classes", "12", "🏫")

    st.divider()

    st.subheader("Quick Access")

    r1c1, r1c2, r1c3, r1c4 = st.columns(4)

    with r1c1:
        module_card("Students", "🎓")

    with r1c2:
        module_card("Teachers", "👩‍🏫")

    with r1c3:
        module_card("Parents", "👨‍👩‍👧")

    with r1c4:
        module_card("Attendance", "📅")

    r2c1, r2c2, r2c3, r2c4 = st.columns(4)

    with r2c1:
        module_card("Fees", "💰")

    with r2c2:
        module_card("Exams", "📝")

    with r2c3:
        module_card("Library", "📚")

    with r2c4:
        module_card("Reports", "📊")