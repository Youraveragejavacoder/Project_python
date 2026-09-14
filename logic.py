class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

class GradeManager:
    def __init__(self, db):
        self.db = db

    def add_student(self, student_id, name):
        self.db.add_student(student_id, name)

    def add_grade(self, student_id, grade):
        self.db.add_grade(student_id, grade)

    def get_average_grade(self, student_id):
        grades = self.db.get_grades(student_id)
        if not grades:
            return 0
        return sum(grades) / len(grades)
