import bcrypt
from database.database import Database


class Authentication:

    def __init__(self):
        self.db = Database()
        self.db.connect()

    # -----------------------------
    # Hash Password
    # -----------------------------
    def hash_password(self, password):

        return bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

    # -----------------------------
    # Verify Password
    # -----------------------------
    def verify_password(self, password, hashed_password):

        return bcrypt.checkpw(
            password.encode(),
            hashed_password.encode()
        )

    # -----------------------------
    # Login
    # -----------------------------
    def login(self, username, password, role):

        query = """
        SELECT id, username, password, role
        FROM users
        WHERE username=%s
        AND role=%s
        """

        self.db.execute(query, (username, role))

        user = self.db.fetchone()

        if user:

            if self.verify_password(password, user[2]):

                return {
                    "success": True,
                    "id": user[0],
                    "username": user[1],
                    "role": user[3]
                }

        return {
            "success": False
        }