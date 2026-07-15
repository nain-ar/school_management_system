import bcrypt
from database.database import Database
SCHOOL_NAME = "ABCPS"

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

    SCHOOL_NAME = "ABCPS"      # Change to your school name
    def login(self, username, password, role):

    # ----------------------------
    # Admin Login
    # ----------------------------
        if role == "Admin":

            self.db.execute("""
                SELECT id, username, password, role
                FROM users
                WHERE username=? AND role='Admin'
            """, (username,))

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

        # ----------------------------
        # Student Login
        # ----------------------------
        elif role == "Student":

            self.db.execute("""
                SELECT student_id,
                    admission_no,
                    first_name,
                    last_name
                FROM students
                WHERE admission_no=?
            """, (username,))

            student = self.db.fetchone()

            if not student:
                return {"success": False}

            expected_password = f"{student[1]}@{SCHOOL_NAME}"


# }  
            if password == expected_password:
                return {
        "success": True,
        "id": student[0],
        "username": student[1],   # Admission Number
        "admission_no": student[1],
        "role": "Student"
    }

            return {"success": False}

        # ----------------------------
        # Teacher Login
        # ----------------------------
        elif role == "Teacher":

            self.db.execute("""
                SELECT teacher_id,
                    employee_id,
                    first_name,
                    last_name,
                    department,
                    joining_date
                FROM teachers
                WHERE employee_id=?
            """, (username,))

            teacher = self.db.fetchone()

            if not teacher:
                return {"success": False}

            joining = str(teacher[5]).replace("-", "")

            expected_password = f"{teacher[3]}@{SCHOOL_NAME}"

            if password == expected_password:
                return {
                    "success": True,
                    "id": teacher[0],
                    "username": teacher[2] + " " + (teacher[3] or ""),
                    "role": "Teacher"
                }

            return {"success": False}

        # ----------------------------
        # Parent Login
        # ----------------------------
        elif role == "Parent":

            self.db.execute("""
                SELECT
                    p.parent_id,
                    p.father_name,
                    p.phone,
                    s.admission_no
                FROM parents p
                JOIN students s
                    ON p.student_id = s.student_id
                WHERE s.admission_no = ?
            """, (username,))

            parent = self.db.fetchone()

            if not parent:
                return {"success": False}

            # Password = Parent's registered phone number
            expected_password = str(parent[2])

            if password == expected_password:
                return {
                    "success": True,
                    "id": parent[0],
                    "username": parent[1],
                    "admission_no": parent[3],
                    "role": "Parent"
                }

            return {"success": False}
    # -----------------------------
    # Close Database
    # -----------------------------
    def close(self):
        self.db.close()