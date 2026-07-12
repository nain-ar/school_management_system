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
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

    # -----------------------------
    # Verify Password
    # -----------------------------
    def verify_password(self, password, hashed_password):
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )

    # -----------------------------
    # Register User
    # -----------------------------
    def register(self, username, password, role):

        self.db.execute(
            "SELECT id FROM users WHERE username=?",
            (username,)
        )

        user = self.db.fetchone()

        if user:
            return {
                "success": True,
                "message": "User already exists."
            }

        hashed_password = self.hash_password(password)

        self.db.execute(
            """
            INSERT INTO users(username, password, role)
            VALUES (?, ?, ?)
            """,
            (username, hashed_password, role)
        )

        return {
            "success": True,
            "message": "Registration Successful."
        }

    # -----------------------------
    # Login
    # -----------------------------
    def login(self, username, password, role):

        self.db.execute(
            """
            SELECT id, username, password, role
            FROM users
            WHERE username=? AND role=?
            """,
            (username, role)
        )

        user = self.db.fetchone()

        if not user:
            return {"success": False}

        if self.verify_password(password, user[2]):
            return {
                "success": True,
                "id": user[0],
                "username": user[1],
                "role": user[3]
            }

        return {"success": False}

    # -----------------------------
    # Close Database
    # -----------------------------
    def close(self):
        self.db.close()