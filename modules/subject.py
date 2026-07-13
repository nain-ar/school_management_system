from database.database import Database


class Subject:

    def __init__(self):
        self.db = Database()
        self.db.connect()

    # ==========================
    # Add Subject
    # ==========================
    def add_subject(
        self,
        subject_code,
        subject_name,
        class_name,
        teacher_id,
        credits
    ):

        query = """
        INSERT INTO subjects(
            subject_code,
            subject_name,
            class_name,
            teacher_id,
            credits
        )
        VALUES(?,?,?,?,?)
        """

        self.db.execute(query, (
            subject_code,
            subject_name,
            class_name,
            teacher_id,
            credits
        ))

    # ==========================
    # View Subjects
    # ==========================
    def get_all_subjects(self):

        self.db.execute("""
            SELECT *
            FROM subjects
            ORDER BY subject_id DESC
        """)

        return self.db.fetchall()

    # ==========================
    # Search Subject
    # ==========================
    def search_subject(self, keyword):

        value = f"%{keyword}%"

        self.db.execute("""
            SELECT *
            FROM subjects
            WHERE subject_code LIKE ?
               OR subject_name LIKE ?
               OR class_name LIKE ?
        """, (
            value,
            value,
            value
        ))

        return self.db.fetchall()

    # ==========================
    # Delete Subject
    # ==========================
    def delete_subject(self, subject_id):

        self.db.execute(
            "DELETE FROM subjects WHERE subject_id=?",
            (subject_id,)
        )

    # ==========================
    # Total Subjects
    # ==========================
    def total_subjects(self):

        self.db.execute(
            "SELECT COUNT(*) FROM subjects"
        )

        result = self.db.fetchone()

        return result[0] if result else 0