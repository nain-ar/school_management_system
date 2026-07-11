import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

class Database:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )

            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                return True

        except Error as e:
            print("Database Error:", e)
            return False

    def execute(self, query, values=None):
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)

            self.connection.commit()

        except Error as e:
            print("Execute Error:", e)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()