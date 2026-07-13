from database.database import Database


class Teacher:

    def __init__(self):
        self.db = Database()
        self.db.connect()

    # ==========================
    # Add Teacher
    # ==========================
    def add_teacher(
        self,
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
        salary,
        photo=None
    ):

        query = """
        INSERT INTO teachers(
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
            salary,
            photo
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """

        self.db.execute(query, (
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
            salary,
            photo
        ))

    # ==========================
    # Get All Teachers
    # ==========================
    def get_all_teachers(self):

        self.db.execute(
            "SELECT * FROM teachers ORDER BY teacher_id DESC"
        )

        return self.db.fetchall()

    # ==========================
    # Search Teacher
    # ==========================
    def search_teacher(self, keyword):

        query = """
        SELECT *
        FROM teachers
        WHERE employee_id LIKE ?
           OR first_name LIKE ?
           OR last_name LIKE ?
           OR department LIKE ?
           OR designation LIKE ?
        """

        value = f"%{keyword}%"

        self.db.execute(
            query,
            (value, value, value, value, value)
        )

        return self.db.fetchall()

    # ==========================
    # Delete Teacher
    # ==========================
    def delete_teacher(self, teacher_id):

        self.db.execute(
            "DELETE FROM teachers WHERE teacher_id=?",
            (teacher_id,)
        )

    # ==========================
    # Total Teachers
    # ==========================
    def total_teachers(self):

        self.db.execute(
            "SELECT COUNT(*) FROM teachers"
        )

        result = self.db.fetchone()

        return result[0] if result else 0