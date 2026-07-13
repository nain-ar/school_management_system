from database.database import Database


class ClassManagement:

    def __init__(self):
        self.db = Database()
        self.db.connect()

    # ==========================
    # Add Class
    # ==========================
    def add_class(
        self,
        class_name,
        section,
        class_teacher,
        room_number,
        capacity
    ):

        query = """
        INSERT INTO classes(
            class_name,
            section,
            class_teacher,
            room_number,
            capacity
        )
        VALUES(?,?,?,?,?)
        """

        self.db.execute(query, (
            class_name,
            section,
            class_teacher,
            room_number,
            capacity
        ))

    # ==========================
    # View Classes
    # ==========================
    def get_all_classes(self):

        self.db.execute("""
            SELECT *
            FROM classes
            ORDER BY class_id DESC
        """)

        return self.db.fetchall()

    # ==========================
    # Search Class
    # ==========================
    def search_class(self, keyword):

        value = f"%{keyword}%"

        self.db.execute("""
            SELECT *
            FROM classes
            WHERE class_name LIKE ?
               OR section LIKE ?
               OR room_number LIKE ?
        """, (
            value,
            value,
            value
        ))

        return self.db.fetchall()

    # ==========================
    # Delete Class
    # ==========================
    def delete_class(self, class_id):

        self.db.execute(
            "DELETE FROM classes WHERE class_id=?",
            (class_id,)
        )

    # ==========================
    # Total Classes
    # ==========================
    def total_classes(self):

        self.db.execute(
            "SELECT COUNT(*) FROM classes"
        )

        result = self.db.fetchone()

        return result[0] if result else 0