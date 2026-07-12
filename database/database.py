import sqlite3
import os


class Database:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            # Create database folder if it doesn't exist
            os.makedirs("database", exist_ok=True)

            # Connect to SQLite database
            self.connection = sqlite3.connect("database/school_management.db")
            self.cursor = self.connection.cursor()

            print("Connected to SQLite successfully!")
            return True

        except sqlite3.Error as e:
            print("Database Error:", e)
            return False

    def execute(self, query, values=None):
        try:
            if values is not None:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)

            self.connection.commit()

        except sqlite3.Error as e:
            print("Execute Error:", e)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()