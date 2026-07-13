from database.database import Database


class Library:

    def __init__(self):
        self.db = Database()
        self.db.connect()

    # ==========================
    # Add Book
    # ==========================
    def add_book(
        self,
        book_code,
        book_name,
        author,
        publisher,
        category,
        quantity,
        available_quantity,
        shelf_no
    ):

        query = """
        INSERT INTO library(
            book_code,
            book_name,
            author,
            publisher,
            category,
            quantity,
            available_quantity,
            shelf_no
        )
        VALUES(?,?,?,?,?,?,?,?)
        """

        self.db.execute(query, (
            book_code,
            book_name,
            author,
            publisher,
            category,
            quantity,
            available_quantity,
            shelf_no
        ))

    # ==========================
    # View Books
    # ==========================
    def get_all_books(self):

        self.db.execute("""
            SELECT *
            FROM library
            ORDER BY book_id DESC
        """)

        return self.db.fetchall()

    # ==========================
    # Search Book
    # ==========================
    def search_book(self, keyword):

        value = f"%{keyword}%"

        self.db.execute("""
            SELECT *
            FROM library
            WHERE book_name LIKE ?
               OR author LIKE ?
               OR category LIKE ?
               OR book_code LIKE ?
        """, (
            value,
            value,
            value,
            value
        ))

        return self.db.fetchall()

    # ==========================
    # Delete Book
    # ==========================
    def delete_book(self, book_id):

        self.db.execute(
            "DELETE FROM library WHERE book_id=?",
            (book_id,)
        )