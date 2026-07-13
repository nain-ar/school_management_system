from database.database import Database


class Exam:

    def __init__(self):
        self.db = Database()
        self.db.connect()

    # ==========================
    # Add Exam
    # ==========================
    def add_exam(
        self,
        exam_name,
        class_name,
        subject_id,
        exam_date,
        total_marks,
        passing_marks
    ):

        query = """
        INSERT INTO exams(
            exam_name,
            class_name,
            subject_id,
            exam_date,
            total_marks,
            passing_marks
        )
        VALUES(?,?,?,?,?,?)
        """

        self.db.execute(query, (
            exam_name,
            class_name,
            subject_id,
            exam_date,
            total_marks,
            passing_marks
        ))

    # ==========================
    # View Exams
    # ==========================
    def get_all_exams(self):

        self.db.execute("""
            SELECT *
            FROM exams
            ORDER BY exam_id DESC
        """)

        return self.db.fetchall()

    # ==========================
    # Search Exam
    # ==========================
    def search_exam(self, keyword):

        value = f"%{keyword}%"

        self.db.execute("""
            SELECT *
            FROM exams
            WHERE exam_name LIKE ?
               OR class_name LIKE ?
        """, (value, value))

        return self.db.fetchall()

    # ==========================
    # Delete Exam
    # ==========================
    def delete_exam(self, exam_id):

        self.db.execute(
            "DELETE FROM exams WHERE exam_id=?",
            (exam_id,)
        )

    # ==========================
    # Total Exams
    # ==========================
    def total_exams(self):

        self.db.execute(
            "SELECT COUNT(*) FROM exams"
        )

        result = self.db.fetchone()

        return result[0] if result else 0