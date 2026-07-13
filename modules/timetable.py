from database.database import Database


class Timetable:

    def __init__(self):
        self.db = Database()
        self.db.connect()

    # =====================================
    # Add Timetable
    # =====================================
    def add_timetable(
        self,
        class_name,
        section,
        subject_id,
        teacher_id,
        day,
        start_time,
        end_time
    ):

        query = """
        INSERT INTO timetable(
            class_name,
            section,
            subject_id,
            teacher_id,
            day,
            start_time,
            end_time
        )
        VALUES(?,?,?,?,?,?,?)
        """

        self.db.execute(query, (
            class_name,
            section,
            subject_id,
            teacher_id,
            day,
            start_time,
            end_time
        ))

    # =====================================
    # View Timetable
    # =====================================
    def get_all_timetable(self):

        self.db.execute("""
            SELECT *
            FROM timetable
            ORDER BY timetable_id DESC
        """)

        return self.db.fetchall()

    # =====================================
    # Search Timetable
    # =====================================
    def search_timetable(self, keyword):

        value = f"%{keyword}%"

        self.db.execute("""
            SELECT *
            FROM timetable
            WHERE class_name LIKE ?
               OR section LIKE ?
               OR day LIKE ?
        """, (
            value,
            value,
            value
        ))

        return self.db.fetchall()

    # =====================================
    # Delete Timetable
    # =====================================
    def delete_timetable(self, timetable_id):

        self.db.execute(
            "DELETE FROM timetable WHERE timetable_id=?",
            (timetable_id,)
        )