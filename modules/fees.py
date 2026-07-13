from database.database import Database

class Fees:

    def __init__(self):
        self.db = Database()
        self.db.connect()

    # ==========================
    # Add Fee
    # ==========================
    def add_fee(
        self,
        student_id,
        fee_type,
        amount,
        paid_amount,
        due_amount,
        payment_date,
        status
    ):

        query = """
        INSERT INTO fees(
            student_id,
            fee_type,
            amount,
            paid_amount,
            due_amount,
            payment_date,
            status
        )
        VALUES(?,?,?,?,?,?,?)
        """

        self.db.execute(query, (
            student_id,
            fee_type,
            amount,
            paid_amount,
            due_amount,
            payment_date,
            status
        ))

    # ==========================
    # View Fees
    # ==========================
    def get_all_fees(self):

        self.db.execute("""
            SELECT *
            FROM fees
            ORDER BY fee_id DESC
        """)

        return self.db.fetchall()

    # ==========================
    # Search Fee
    # ==========================
    def search_fee(self, keyword):

        value = f"%{keyword}%"

        self.db.execute("""
            SELECT *
            FROM fees
            WHERE student_id LIKE ?
               OR fee_type LIKE ?
               OR status LIKE ?
        """, (
            value,
            value,
            value
        ))

        return self.db.fetchall()

    # ==========================
    # Delete Fee
    # ==========================
    def delete_fee(self, fee_id):

        self.db.execute(
            "DELETE FROM fees WHERE fee_id=?",
            (fee_id,)
        )

    # ==========================
    # Total Fees
    # ==========================
    def total_fees(self):

        self.db.execute(
            "SELECT COUNT(*) FROM fees"
        )

        result = self.db.fetchone()

        return result[0] if result else 0