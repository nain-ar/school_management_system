from database.database import Database


class IDCard:

    def __init__(self):
        self.db = Database()
        self.db.connect()
    def get_admission_numbers(self):
        self.db.execute("""
            SELECT admission_no
            FROM students
            ORDER BY admission_no
        """)
        return [row[0] for row in self.db.fetchall()]
    def get_student_by_admission(self, admission_no):

        query = """
        SELECT
            s.admission_no,
            s.first_name,
            s.last_name,
            s.class_name,
            s.section,
            s.photo,
            p.phone
        FROM students s
        LEFT JOIN parents p
            ON s.student_id = p.student_id
        WHERE s.admission_no = ?
        """

    

        self.db.execute(query, (admission_no,))

        return self.db.fetchone()