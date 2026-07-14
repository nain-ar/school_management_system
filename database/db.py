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
        employee_id TEXT UNIQUE NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT,
        gender TEXT CHECK(gender IN ('Male','Female','Other')),
        dob DATE,
        phone TEXT,
        email TEXT,
        address TEXT,
        qualification TEXT,
        department TEXT,
        designation TEXT,
        joining_date DATE,
        salary REAL,
        photo TEXT,
        status TEXT DEFAULT 'Active'
            CHECK(status IN ('Active','Inactive')),
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
        db.execute("""
CREATE TABLE IF NOT EXISTS library(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_code TEXT UNIQUE NOT NULL,
    book_name TEXT NOT NULL,
    author TEXT,
    publisher TEXT,
    category TEXT,
    quantity INTEGER DEFAULT 1,
    available_quantity INTEGER DEFAULT 1,
    shelf_no TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
        db.execute("""
CREATE TABLE IF NOT EXISTS library_issues(
    issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    issue_date DATE,
    return_date DATE,
    fine REAL DEFAULT 0,
    status TEXT DEFAULT 'Issued'
        CHECK(status IN ('Issued','Returned')),
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(book_id) REFERENCES library(book_id)
)
""")
        db.execute("""
CREATE TABLE IF NOT EXISTS subjects(
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_code TEXT UNIQUE NOT NULL,
    subject_name TEXT NOT NULL,
    class_name TEXT NOT NULL,
    teacher_id INTEGER,
    credits INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(teacher_id) REFERENCES teachers(teacher_id)
)""")
        db.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    class_name TEXT,
    attendance_date DATE,
    status TEXT
        CHECK(status IN ('Present','Absent','Late')),
    remarks TEXT,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)""")
        db.execute("""CREATE TABLE IF NOT EXISTS classes(
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL,
    section TEXT NOT NULL,
    class_teacher INTEGER,
    room_number TEXT,
    capacity INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(class_teacher) REFERENCES teachers(teacher_id)
)""")
        
        db.execute("""CREATE TABLE IF NOT EXISTS exams(
    exam_id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_name TEXT,
    class_name TEXT,
    subject_id INTEGER,
    exam_date DATE,
    total_marks INTEGER,
    passing_marks INTEGER,
    FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
)""")
        db.execute("""CREATE TABLE IF NOT EXISTS results(
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    exam_id INTEGER,
    marks_obtained REAL,
    grade TEXT,
    remarks TEXT,
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(exam_id) REFERENCES exams(exam_id)
)""")
        db.execute("""CREATE TABLE IF NOT EXISTS fees(
    fee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    fee_type TEXT,
    amount REAL,
    paid_amount REAL DEFAULT 0,
    due_amount REAL,
    payment_date DATE,
    status TEXT
        CHECK(status IN ('Paid','Pending','Partial')),
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)""")
        db.execute("""CREATE TABLE IF NOT EXISTS timetable(
    timetable_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT,
    section TEXT,
    subject_id INTEGER,
    teacher_id INTEGER,
    day TEXT,
    start_time TEXT,
    end_time TEXT,
    FOREIGN KEY(subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY(teacher_id) REFERENCES teachers(teacher_id)
)""")
        db.execute("""CREATE TABLE IF NOT EXISTS notices(
    notice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    notice_date DATE,
    audience TEXT
        CHECK(audience IN ('All','Students','Teachers','Parents')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)""")
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