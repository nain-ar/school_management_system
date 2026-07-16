import streamlit as st
import pandas as pd
from database.database import Database


def show_teacher_dashboard():

    # =====================================
    # Session State
    # =====================================
    if "teacher_page" not in st.session_state:
        st.session_state.teacher_page = "dashboard"

    db = Database()
    db.connect()

    # =====================================
    # CSS
    # =====================================
    st.markdown("""
    <style>

    div.stButton > button{
        width:100%;
        height:90px;
        border-radius:15px;
        border:1px solid #E5E7EB;
        background:white;
        box-shadow:0 4px 10px rgba(0,0,0,.08);
        font-size:18px;
        font-weight:600;
        margin-bottom:12px;
    }

    div.stButton > button:hover{
        transform:translateY(-3px);
        border-color:#4CAF50;
    }

    </style>
    """, unsafe_allow_html=True)

    # =====================================
    # MY PROFILE
    # =====================================
    if st.session_state.teacher_page == "profile":

        st.title("👤 My Profile")

        name = st.session_state.username.split()

        first = name[0]
        last = ""

        if len(name) > 1:
            last = name[1]

        db.execute("""
        SELECT
            employee_id,
            first_name,
            last_name,
            gender,
            dob,
            phone,
            email,
            address,
            qualification,
            department,
            designation,
            joining_date,
            salary
        FROM teachers
        WHERE first_name=? AND last_name=?
        """,(first,last))

        teacher = db.fetchone()

        if teacher:

            c1,c2 = st.columns(2)

            with c1:
                st.metric("Employee ID",teacher[0])
                st.metric("Teacher",teacher[1]+" "+(teacher[2] or ""))
                st.metric("Gender",teacher[3])
                st.metric("DOB",teacher[4])

            with c2:
                st.metric("Department",teacher[9])
                st.metric("Designation",teacher[10])
                st.metric("Joining",teacher[11])
                st.metric("Salary",teacher[12])

            st.divider()

            st.write("### Contact")

            st.write("**Phone:**",teacher[5])
            st.write("**Email:**",teacher[6])
            st.write("**Address:**",teacher[7])

            st.divider()

            st.write("### Qualification")

            st.success(teacher[8])

        else:
            st.error("Teacher not found.")

        if st.button("⬅ Back",use_container_width=True):
            st.session_state.teacher_page="dashboard"
            db.close()
            st.rerun()

        db.close()
        return
        # ======================================================
    # MY STUDENTS
    # ======================================================
    elif st.session_state.teacher_page == "students":

        st.title("👨‍🎓 My Students")

        teacher_id = st.session_state.teacher_id

        # Check if teacher is Class Teacher
        db.execute("""
            SELECT class_name, section
            FROM classes
            WHERE class_teacher = ?
        """, (teacher_id,))

        class_info = db.fetchone()

        if class_info:

            st.success(
                f"You are the Class Teacher of "
                f"{class_info[0]} - {class_info[1]}"
            )

            db.execute("""
                SELECT
                    admission_no,
                    first_name,
                    last_name,
                    class_name,
                    section,
                    roll_no
                FROM students
                WHERE class_name=? AND section=?
                ORDER BY roll_no
            """, (class_info[0], class_info[1]))

        else:

            # Subject Teacher
            db.execute("""
                SELECT DISTINCT
                    class_name
                FROM subjects
                WHERE teacher_id = ?
            """, (teacher_id,))

            classes = db.fetchall()

            if not classes:
                st.info("No students assigned.")

                if st.button("⬅ Back", use_container_width=True):
                    st.session_state.teacher_page = "dashboard"
                    db.close()
                    st.rerun()

                db.close()
                return

            class_names = [c[0] for c in classes]

            placeholders = ",".join(["?"] * len(class_names))

            db.execute(f"""
                SELECT
                    admission_no,
                    first_name,
                    last_name,
                    class_name,
                    section,
                    roll_no
                FROM students
                WHERE class_name IN ({placeholders})
                ORDER BY class_name, roll_no
            """, tuple(class_names))

        students = db.fetchall()

        if students:

            df = pd.DataFrame(
                students,
                columns=[
                    "Admission No",
                    "First Name",
                    "Last Name",
                    "Class",
                    "Section",
                    "Roll No"
                ]
            )

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            st.success(f"Total Students : {len(df)}")

        else:
            st.info("No students found.")

        if st.button("⬅ Back", key="students_back", use_container_width=True):
            st.session_state.teacher_page = "dashboard"
            db.close()
            st.rerun()

        db.close()
        return


    # ======================================================
    # MY SUBJECTS
    # ======================================================
    elif st.session_state.teacher_page == "subjects":

        st.title("📚 My Subjects")

        db.execute("""
            SELECT
                subject_code,
                subject_name,
                class_name,
                credits
            FROM subjects
            WHERE teacher_id = ?
            ORDER BY class_name
        """, (st.session_state.teacher_id,))

        subjects = db.fetchall()

        if subjects:

            df = pd.DataFrame(
                subjects,
                columns=[
                    "Subject Code",
                    "Subject",
                    "Class",
                    "Credits"
                ]
            )

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

        else:
            st.info("No subjects assigned.")

        if st.button("⬅ Back", key="subjects_back", use_container_width=True):
            st.session_state.teacher_page = "dashboard"
            db.close()
            st.rerun()

        db.close()
        return
        # ======================================================
    # ATTENDANCE
    # ======================================================
    elif st.session_state.teacher_page == "attendance":

        st.title("📅 Student Attendance")

        teacher_id = st.session_state.teacher_id

        # Find teacher's class
        db.execute("""
            SELECT class_name, section
            FROM classes
            WHERE class_teacher=?
        """, (teacher_id,))

        class_info = db.fetchone()

        if class_info:

            db.execute("""
                SELECT
                    admission_no,
                    first_name,
                    last_name,
                    student_id
                FROM students
                WHERE class_name=? AND section=?
                ORDER BY roll_no
            """, (class_info[0], class_info[1]))

            students = db.fetchall()

            if students:

                st.write(f"### {class_info[0]} - {class_info[1]}")

                attendance_date = st.date_input("Attendance Date")

                for student in students:

                    status = st.selectbox(
                        f"{student[1]} {student[2]} ({student[0]})",
                        ["Present", "Absent", "Late"],
                        key=f"attendance_{student[3]}"
                    )

                    db.execute("""
                        SELECT attendance_id
                        FROM attendance
                        WHERE student_id=? AND attendance_date=?
                    """, (student[3], attendance_date))

                    existing = db.fetchone()

                    if existing:
                        db.execute("""
                            UPDATE attendance
                            SET status=?
                            WHERE attendance_id=?
                        """, (status, existing[0]))
                    else:
                        db.execute("""
                            INSERT INTO attendance(
                                student_id,
                                class_name,
                                attendance_date,
                                status
                            )
                            VALUES(?,?,?,?)
                        """, (
                            student[3],
                            class_info[0],
                            attendance_date,
                            status
                        ))

                if st.button("💾 Save Attendance", use_container_width=True):
                    st.success("Attendance Saved Successfully!")

            else:
                st.info("No students found.")

        else:
            st.info("Only Class Teachers can mark attendance.")

        if st.button("⬅ Back", key="attendance_back"):
            st.session_state.teacher_page = "dashboard"
            db.close()
            st.rerun()

        db.close()
        return


    # ======================================================
    # NOTICES
    # ======================================================
    elif st.session_state.teacher_page == "notices":

        st.title("📢 School Notices")

        db.execute("""
            SELECT
                title,
                description,
                notice_date,
                audience
            FROM notices
            WHERE audience='All'
               OR audience='Teachers'
            ORDER BY notice_date DESC
        """)

        notices = db.fetchall()

        if notices:

            for notice in notices:

                with st.expander(f"{notice[0]} ({notice[2]})"):

                    st.write(notice[1])
                    st.caption(f"Audience : {notice[3]}")

        else:
            st.info("No notices available.")

        if st.button("⬅ Back", key="notice_back"):
            st.session_state.teacher_page = "dashboard"
            db.close()
            st.rerun()

        db.close()
        return


    # ======================================================
    # DASHBOARD
    # ======================================================

    st.title("👩‍🏫 Teacher Dashboard")
    st.write(f"Welcome **{st.session_state.username}** 👋")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👤 My Profile", use_container_width=True):
            st.session_state.teacher_page = "profile"
            st.rerun()

    with col2:
        if st.button("👨‍🎓 My Students", use_container_width=True):
            st.session_state.teacher_page = "students"
            st.rerun()

    col3, col4 = st.columns(2)

    with col3:
        if st.button("📚 My Subjects", use_container_width=True):
            st.session_state.teacher_page = "subjects"
            st.rerun()

    with col4:
        if st.button("📅 Attendance", use_container_width=True):
            st.session_state.teacher_page = "attendance"
            st.rerun()

    col5, col6 = st.columns(2)

    with col5:
        if st.button("📢 Notices", use_container_width=True):
            st.session_state.teacher_page = "notices"
            st.rerun()

    with col6:
        if st.button("🚪 Logout", use_container_width=True):

            db.close()

            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.role = ""
            st.session_state.teacher_page = "dashboard"

            if "teacher_id" in st.session_state:
                del st.session_state["teacher_id"]

            if "employee_id" in st.session_state:
                del st.session_state["employee_id"]

            st.session_state.page = "welcome"

            st.rerun()

    db.close()