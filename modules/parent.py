from database.database import Database


class Parent:

    def __init__(self):
        self.db = Database()
        self.db.connect()

    # ==========================
    # Add Parent
    # ==========================
    def add_parent(
        self,
        student_id,
        father_name,
        mother_name,
        phone,
        email,
        address
    ):

        query = """
        INSERT INTO parents(
            student_id,
            father_name,
            mother_name,
            phone,
            email,
            address
        )
        VALUES(?,?,?,?,?,?)
        """

        self.db.execute(query, (
            student_id,
            father_name,
            mother_name,
            phone,
            email,
            address
        ))

    # ==========================
    # View Parents
    # ==========================
    def get_all_parents(self):

        self.db.execute("""
            SELECT
                parent_id,
                student_id,
                father_name,
                mother_name,
                phone,
                email,
                address
            FROM parents
            ORDER BY parent_id DESC
        """)

        return self.db.fetchall()

    # ==========================
    # Search Parent
    # ==========================
    def search_parent(self, keyword):

        value = f"%{keyword}%"

        self.db.execute("""
            SELECT *
            FROM parents
            WHERE father_name LIKE ?
               OR mother_name LIKE ?
               OR phone LIKE ?
               OR email LIKE ?
        """, (
            value,
            value,
            value,
            value
        ))

        return self.db.fetchall()

    # ==========================
    # Delete Parent
    # ==========================
    def delete_parent(self, parent_id):

        self.db.execute(
            "DELETE FROM parents WHERE parent_id=?",
            (parent_id,)
        )

    # ==========================
    # Total Parents
    # ==========================
    def total_parents(self):

        self.db.execute(
            "SELECT COUNT(*) FROM parents"
        )

        result = self.db.fetchone()

        return result[0] if result else 0