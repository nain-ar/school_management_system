import streamlit as st
import pandas as pd
from database.database import Database


def show_parent_dashboard():

    # ==========================
    # Session State
    # ==========================
    if "parent_page" not in st.session_state:
        st.session_state.parent_page = "dashboard"

    # ==========================
    # CSS
    # ==========================
    st.markdown("""
    <style>

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

    db = Database()
    db.connect()

    # ======================================================
    # WARD PROFILE
    # ======================================================
    if st.session_state.parent_page == "ward_profile":

        st.title("👦 Ward Profile")

        db.execute("""
        SELECT
            s.admission_no,
            s.first_name,
            s.last_name,
            s.gender,
            s.dob,
            s.phone,
            s.email,
            s.address,
            s.class_name,
            s.section,
            s.roll_no,
            p.father_name,
            p.mother_name,
            p.phone
        FROM students s
        JOIN parents p
        ON s.student_id = p.student_id
        WHERE s.admission_no = ?
        """, (st.session_state.admission_no,))

        student = db.fetchone()

        if student:

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Admission No", student[0])
                st.metric("Student", f"{student[1]} {student[2]}")
                st.metric("Gender", student[3])
                st.metric("DOB", student[4])

            with col2:
                st.metric("Class", f"{student[8]}-{student[9]}")
                st.metric("Roll No", student[10])
                st.metric("Phone", student[5])
                st.metric("Email", student[6])

            st.write("### Address")
            st.info(student[7])

            st.write("### Parent Details")

            c1, c2 = st.columns(2)

            with c1:
                st.success(f"Father : {student[11]}")

            with c2:
                st.success(f"Mother : {student[12]}")

            st.info(f"Parent Phone : {student[13]}")

        else:
            st.error("Ward not found.")

        db.close()

        if st.button("⬅ Back", use_container_width=True):
            st.session_state.parent_page = "dashboard"
            st.rerun()

        return
        # ======================================================
    # ATTENDANCE
    # ======================================================
    elif st.session_state.parent_page == "attendance":

        st.title("📅 Ward Attendance")

        db.execute("""
            SELECT student_id
            FROM students
            WHERE admission_no = ?
        """, (st.session_state.admission_no,))

        student = db.fetchone()

        if student:

            db.execute("""
                SELECT
                    attendance_date,
                    status,
                    remarks
                FROM attendance
                WHERE student_id = ?
                ORDER BY attendance_date DESC
            """, (student[0],))

            attendance = db.fetchall()

            if attendance:

                df = pd.DataFrame(
                    attendance,
                    columns=[
                        "Date",
                        "Status",
                        "Remarks"
                    ]
                )

                present = len(df[df["Status"] == "Present"])
                absent = len(df[df["Status"] == "Absent"])
                late = len(df[df["Status"] == "Late"])

                c1, c2, c3 = st.columns(3)

                c1.metric("✅ Present", present)
                c2.metric("❌ Absent", absent)
                c3.metric("⏰ Late", late)

                st.divider()

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

            else:
                st.info("No attendance records found.")

        else:
            st.error("Student not found.")

        if st.button("⬅ Back", key="attendance_back", use_container_width=True):
            st.session_state.parent_page = "dashboard"
            st.rerun()

        return


    # ======================================================
    # FEES
    # ======================================================
    elif st.session_state.parent_page == "fees":

        st.title("💰 Ward Fees")

        db.execute("""
            SELECT student_id
            FROM students
            WHERE admission_no = ?
        """, (st.session_state.admission_no,))

        student = db.fetchone()

        if student:

            db.execute("""
                SELECT
                    fee_type,
                    amount,
                    paid_amount,
                    due_amount,
                    status,
                    payment_date
                FROM fees
                WHERE student_id = ?
            """, (student[0],))

            fees = db.fetchall()

            if fees:

                df = pd.DataFrame(
                    fees,
                    columns=[
                        "Fee Type",
                        "Total",
                        "Paid",
                        "Due",
                        "Status",
                        "Payment Date"
                    ]
                )

                total = df["Total"].sum()
                paid = df["Paid"].sum()
                due = df["Due"].sum()

                c1, c2, c3 = st.columns(3)

                c1.metric("Total Fees", f"₹{total:,.0f}")
                c2.metric("Paid", f"₹{paid:,.0f}")
                c3.metric("Pending", f"₹{due:,.0f}")

                st.divider()

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

            else:
                st.info("No fee records found.")

        else:
            st.error("Student not found.")

        if st.button("⬅ Back", key="fees_back", use_container_width=True):
            st.session_state.parent_page = "dashboard"
            st.rerun()

        return
        # ======================================================
    # RESULTS
    # ======================================================
    elif st.session_state.parent_page == "results":

        st.title("📝 Ward Results")

        db.execute("""
            SELECT student_id
            FROM students
            WHERE admission_no = ?
        """, (st.session_state.admission_no,))

        student = db.fetchone()

        if student:

            db.execute("""
                SELECT
                    e.exam_name,
                    s.subject_name,
                    r.marks_obtained,
                    e.total_marks,
                    r.grade,
                    r.remarks
                FROM results r
                JOIN exams e
                    ON r.exam_id = e.exam_id
                JOIN subjects s
                    ON e.subject_id = s.subject_id
                WHERE r.student_id = ?
                ORDER BY e.exam_name
            """, (student[0],))

            results = db.fetchall()

            if results:

                df = pd.DataFrame(
                    results,
                    columns=[
                        "Exam",
                        "Subject",
                        "Marks",
                        "Total",
                        "Grade",
                        "Remarks"
                    ]
                )

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

            else:
                st.info("No results available.")

        else:
            st.error("Student not found.")

        if st.button("⬅ Back", key="results_back", use_container_width=True):
            st.session_state.parent_page = "dashboard"
            st.rerun()

        return


    # ======================================================
    # DASHBOARD
    # ======================================================

    st.title("👨‍👩‍👧 Parent Dashboard")
    st.write(f"Welcome **{st.session_state.username}** 👋")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👦 Ward Profile", use_container_width=True):
            st.session_state.parent_page = "ward_profile"
            st.rerun()

    with col2:
        if st.button("📅 Attendance", use_container_width=True):
            st.session_state.parent_page = "attendance"
            st.rerun()

    col3, col4 = st.columns(2)

    with col3:
        if st.button("📝 Results", use_container_width=True):
            st.session_state.parent_page = "results"
            st.rerun()

    with col4:
        if st.button("💰 Fees", use_container_width=True):
            st.session_state.parent_page = "fees"
            st.rerun()

    st.divider()

    db.close()

    if st.button(" Logout", use_container_width=True):

        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.session_state.parent_page = "dashboard"

        if "admission_no" in st.session_state:
            del st.session_state["admission_no"]

        st.session_state.page = "welcome"

        st.rerun()