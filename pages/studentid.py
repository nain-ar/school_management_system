import streamlit as st
import qrcode
from io import BytesIO
from modules.studentid import IDCard


def generate_qr(student):

    text = f"""
Admission No : {student[0]}
Name : {student[1]} {student[2]}
Class : {student[3]}-{student[4]}
Parent Mobile : {student[6]}
"""

    qr = qrcode.make(text)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer


def show_id_card():

    db = IDCard()

    admission_numbers = db.get_admission_numbers()

    st.title("🆔 Student ID Card Generator")


    if not admission_numbers:

        st.warning("No Students Found.")
        return


    admission_no = st.selectbox(
        "Select Admission Number",
        admission_numbers
    )


    if st.button("Generate ID Card"):


        student = db.get_student_by_admission(admission_no)


        if student:


            qr = generate_qr(student)


            st.markdown("---")


            st.markdown("""
            <div style="
            border:3px solid #1E88E5;
            border-radius:15px;
            padding:20px;
            background:#F5F9FF;
            ">
            """, unsafe_allow_html=True)


            col1, col2 = st.columns([1,2])


            with col1:

                if student[5]:

                    st.image(
                        student[5],
                        width=150
                    )

                else:

                    st.info("No Photo")


                st.image(
                    qr,
                    width=150
                )


            with col2:


                st.markdown(
                    "## 🏫 ABC PUBLIC SCHOOL"
                )


                st.write(
                    f"**Admission No:** {student[0]}"
                )


                st.write(
                    f"**Name:** {student[1]} {student[2]}"
                )


                st.write(
                    f"**Class:** {student[3]} - {student[4]}"
                )


                st.write(
                    f"**Parent Mobile:** {student[6]}"
                )


            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


        else:

            st.error("Student Not Found.")



    st.divider()


    _, col, _ = st.columns([1,2,1])


    with col:

        if st.button(
            "⬅ Back to Dashboard",
            use_container_width=True
        ):

            st.session_state.page = "dashboard"
            st.rerun()