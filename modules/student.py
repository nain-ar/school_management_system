from database.database import Database


class Student:

    def __init__(self):
        self.db = Database()
        self.db.connect()

    # -----------------------------
    # Add Student
    # -----------------------------
    def add_student(
        self,
        admission_no,
        first_name,
        last_name,
        gender,
        dob,
        phone,
        email,
        address,
        class_name,
        section,
        roll_no,
        admission_date,
        photo="",
        qr_code=""
    ):

        self.db.execute("""
        INSERT INTO students(
            admission_no,
            first_name,
            last_name,
            gender,
            dob,
            phone,
            email,
            address,
            class_name,
            section,
            roll_no,
            admission_date,
            photo,
            qr_code
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            admission_no,
            first_name,
            last_name,
            gender,
            dob,
            phone,
            email,
            address,
            class_name,
            section,
            roll_no,
            admission_date,
            photo,
            qr_code
        ))

    # -----------------------------
    # View All Students
    # -----------------------------
    def get_all_students(self):

        self.db.execute("""
        SELECT *
        FROM students
        ORDER BY student_id DESC
        """)

        return self.db.fetchall()

    # -----------------------------
    # Search Student
    # -----------------------------
    def search_student(self, keyword):

        self.db.execute("""
        SELECT *
        FROM students
        WHERE admission_no LIKE ?
        OR first_name LIKE ?
        OR last_name LIKE ?
        """, (
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%"
        ))

        return self.db.fetchall()

    # -----------------------------
    # Update Student
    # -----------------------------
    def update_student(
        self,
        student_id,
        phone,
        email,
        address
    ):

        self.db.execute("""
        UPDATE students
        SET
            phone=?,
            email=?,
            address=?
        WHERE student_id=?
        """, (
            phone,
            email,
            address,
            student_id
        ))

    # -----------------------------
    # Delete Student
    # -----------------------------
    def delete_student(self, student_id):

        self.db.execute("""
        DELETE FROM students
        WHERE student_id=?
        """, (student_id,))

    # -----------------------------
    # Close Connection
    # -----------------------------
    def close(self):
        self.db.close()