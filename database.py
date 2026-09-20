import sqlite3
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


class Database:
    def __init__(self, db_name="grading_system.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        # User authentication table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id_number TEXT PRIMARY KEY,
                password_hash TEXT NOT NULL
            )
        ''')

        # Student records table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')

        # Grades table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT,
                grade REAL NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (student_id)
            )
        ''')

        self.conn.commit()

    # =========================
    # USER FUNCTIONS
    # =========================

    def user_exists(self, id_number):
        cursor = self.conn.cursor()

        cursor.execute(
            'SELECT 1 FROM users WHERE id_number = ?',
            (id_number,)
        )

        return cursor.fetchone() is not None

    def add_user(self, id_number, password):
        password_hash = hash_password(password)

        cursor = self.conn.cursor()

        cursor.execute(
            'INSERT INTO users (id_number, password_hash) VALUES (?, ?)',
            (id_number, password_hash)
        )

        self.conn.commit()

    def validate_user(self, id_number, password):
        password_hash = hash_password(password)

        cursor = self.conn.cursor()

        cursor.execute(
            'SELECT password_hash FROM users WHERE id_number = ?',
            (id_number,)
        )

        row = cursor.fetchone()

        if row is None:
            return False

        return row[0] == password_hash

    # =========================
    # STUDENT FUNCTIONS
    # =========================

    def add_student(self, student_id, name):
        cursor = self.conn.cursor()

        cursor.execute(
            '''
            INSERT OR REPLACE INTO students (student_id, name)
            VALUES (?, ?)
            ''',
            (student_id, name)
        )

        self.conn.commit()

        # Automatically update text file
        self.export_student_records()

    # =========================
    # GRADE FUNCTIONS
    # =========================

    def add_grade(self, student_id, grade):
        cursor = self.conn.cursor()

        cursor.execute(
            '''
            INSERT INTO grades (student_id, grade)
            VALUES (?, ?)
            ''',
            (student_id, grade)
        )

        self.conn.commit()

        # Automatically update text file
        self.export_student_records()

    def get_grades(self, student_id):
        cursor = self.conn.cursor()

        cursor.execute(
            'SELECT grade FROM grades WHERE student_id = ?',
            (student_id,)
        )

        rows = cursor.fetchall()

        return [row[0] for row in rows]

    # =========================
    # FILE HANDLING
    # =========================

    def export_student_records(self):
        cursor = self.conn.cursor()

        cursor.execute('''
            SELECT student_id, name
            FROM students
        ''')

        students = cursor.fetchall()

        # Creates the file if it does not exist.
        # If it already exists, it updates the contents.
        with open("student_records.txt", "w", encoding="utf-8") as file:

            for student_id, name in students:

                file.write(f"Student ID: {student_id}\n")
                file.write(f"Name: {name}\n")

                cursor.execute(
                    '''
                    SELECT grade
                    FROM grades
                    WHERE student_id = ?
                    ''',
                    (student_id,)
                )

                grades = [row[0] for row in cursor.fetchall()]

                file.write("Grades: ")

                if grades:
                    file.write(
                        ", ".join(str(grade) for grade in grades)
                    )

                    average = sum(grades) / len(grades)

                    file.write(
                        f"\nAverage: {average:.2f}\n"
                    )

                else:
                    file.write("No grades recorded\n")
                    file.write("Average: N/A\n")

                file.write("-" * 30 + "\n")

    # =========================
    # CLOSE DATABASE
    # =========================

    def close(self):
        self.conn.close()


# =========================
# TEST / EXAMPLE
# =========================

if __name__ == "__main__":

    db = Database()

    # Add a student
    db.add_student("2026-0001", "John Doe")

    # Add grades
    db.add_grade("2026-0001", 90)
    db.add_grade("2026-0001", 85)
    db.add_grade("2026-0001", 95)

    # Manually export if needed
    db.export_student_records()

    db.close()

    print("Student records exported successfully!")