from database.database import Database


class Result:

    def __init__(self):
        self.db = Database()
        self.db.connect()

    # ==========================
    # Add Result
    # ==========================
    def add_result(
        self,
        student_id,
        exam_id,
        marks_obtained,
        grade,
        remarks
    ):

        query = """
        INSERT INTO results(
            student_id,
            exam_id,
            marks_obtained,
            grade,
            remarks
        )
        VALUES(?,?,?,?,?)
        """

        self.db.execute(query, (
            student_id,
            exam_id,
            marks_obtained,
            grade,
            remarks
        ))

    # ==========================
    # View Results
    # ==========================
    def get_all_results(self):

        self.db.execute("""
            SELECT *
            FROM results
            ORDER BY result_id DESC
        """)

        return self.db.fetchall()

    # ==========================
    # Search Results
    # ==========================
    def search_result(self, keyword):

        value = f"%{keyword}%"

        self.db.execute("""
            SELECT *
            FROM results
            WHERE student_id LIKE ?
               OR exam_id LIKE ?
               OR grade LIKE ?
        """, (
            value,
            value,
            value
        ))

        return self.db.fetchall()

    # ==========================
    # Delete Result
    # ==========================
    def delete_result(self, result_id):

        self.db.execute(
            "DELETE FROM results WHERE result_id=?",
            (result_id,)
        )

    # ==========================
    # Total Results
    # ==========================
    def total_results(self):

        self.db.execute(
            "SELECT COUNT(*) FROM results"
        )

        result = self.db.fetchone()

        return result[0] if result else 0