from database.database import Database


class Notice:

    def __init__(self):
        self.db = Database()
        self.db.connect()

    # =====================================
    # Add Notice
    # =====================================
    def add_notice(
        self,
        title,
        description,
        notice_date,
        audience
    ):

        query = """
        INSERT INTO notices(
            title,
            description,
            notice_date,
            audience
        )
        VALUES(?,?,?,?)
        """

        self.db.execute(query, (
            title,
            description,
            notice_date,
            audience
        ))

    # =====================================
    # View Notices
    # =====================================
    def get_all_notices(self):

        self.db.execute("""
            SELECT *
            FROM notices
            ORDER BY notice_id DESC
        """)

        return self.db.fetchall()

    # =====================================
    # Search Notice
    # =====================================
    def search_notice(self, keyword):

        value = f"%{keyword}%"

        self.db.execute("""
            SELECT *
            FROM notices
            WHERE title LIKE ?
               OR audience LIKE ?
        """, (
            value,
            value
        ))

        return self.db.fetchall()

    # =====================================
    # Delete Notice
    # =====================================
    def delete_notice(self, notice_id):

        self.db.execute(
            "DELETE FROM notices WHERE notice_id=?",
            (notice_id,)
        )

    # =====================================
    # Total Notices
    # =====================================
    def total_notices(self):

        self.db.execute(
            "SELECT COUNT(*) FROM notices"
        )

        result = self.db.fetchone()

        return result[0] if result else 0