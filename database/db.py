from database.database import Database
import bcrypt


def create_tables():
    db = Database()

    if db.connect():

        # Users Table
        db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('Admin','Teacher','Student','Parent')),
            status TEXT DEFAULT 'Active'
                CHECK(status IN ('Active','Inactive')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Students Table
        db.execute("""
        CREATE TABLE IF NOT EXISTS students(
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            admission_no TEXT UNIQUE NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT,
            gender TEXT CHECK(gender IN ('Male','Female','Other')),
            dob DATE,
            phone TEXT,
            email TEXT,
            address TEXT,
            class_name TEXT,
            section TEXT,
            roll_no TEXT,
            admission_date DATE,
            photo TEXT,
            qr_code TEXT,
            status TEXT DEFAULT 'Active'
                CHECK(status IN ('Active','Inactive')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Teachers Table
        db.execute("""
        CREATE TABLE IF NOT EXISTS teachers(
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            subject TEXT,
            qualification TEXT,
            phone TEXT,
            email TEXT,
            address TEXT,
            photo TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Parents Table
        db.execute("""
        CREATE TABLE IF NOT EXISTS parents(
            parent_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            father_name TEXT,
            mother_name TEXT,
            phone TEXT,
            email TEXT,
            address TEXT,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
        """)

        # Create default admin if it doesn't exist
        db.execute(
            "SELECT id FROM users WHERE username=?",
            ("admin",)
        )

        if db.fetchone() is None:
            hashed = bcrypt.hashpw(
                "admin123".encode(),
                bcrypt.gensalt()
            ).decode()

            db.execute(
                """
                INSERT INTO users(username, password, role)
                VALUES (?, ?, ?)
                """,
                ("admin", hashed, "Admin")
            )

            print("Default Admin Created")

        db.close()
        print("Database created successfully!")


if __name__ == "__main__":
    create_tables()