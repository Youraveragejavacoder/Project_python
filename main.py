from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt
import sys

class StudentGradingSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Grading System")
        self.setup_ui()

    def setup_ui(self):
        # Labels and input fields
        self.name_label = QLabel("Student Name:")
        self.name_input = QLineEdit()

        self.id_label = QLabel("Student ID:")
        self.id_input = QLineEdit()

        self.grade_labels = []
        self.grade_inputs = []
        for i in range(1, 4):  # 3 grades for example
            label = QLabel(f"Grade {i}:")
            input_field = QLineEdit()
            input_field.setPlaceholderText("0 - 100")
            self.grade_labels.append(label)
            self.grade_inputs.append(input_field)

        # Calculate button
        self.calc_button = QPushButton("Calculate Grade")
        self.calc_button.clicked.connect(self.calculate_grade)

        # Result output label
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Arrange layout
        main_layout = QVBoxLayout()

        # Student info layout
        info_layout = QHBoxLayout()
        info_layout.addWidget(self.name_label)
        info_layout.addWidget(self.name_input)
        main_layout.addLayout(info_layout)

        id_layout = QHBoxLayout()
        id_layout.addWidget(self.id_label)
        id_layout.addWidget(self.id_input)
        main_layout.addLayout(id_layout)

        # Grades layout
        for label, input_field in zip(self.grade_labels, self.grade_inputs):
            grade_layout = QHBoxLayout()
            grade_layout.addWidget(label)
            grade_layout.addWidget(input_field)
            main_layout.addLayout(grade_layout)

        main_layout.addWidget(self.calc_button)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def calculate_grade(self):
        name = self.name_input.text().strip()
        student_id = self.id_input.text().strip()

        if not name or not student_id:
            QMessageBox.warning(self, "Input Error", "Please enter both student name and ID.")
            return

        grades = []
        for input_field in self.grade_inputs:
            try:
                grade = float(input_field.text())
                if grade < 0 or grade > 100:
                    raise ValueError("Grade out of range")
                grades.append(grade)
            except ValueError:
                QMessageBox.warning(self, "Input Error", "Please enter valid grades between 0 and 100.")
                return

        average = sum(grades) / len(grades)
        letter_grade = self.get_letter_grade(average)

        result_text = (
            f"Student: {name} (ID: {student_id})\n"
            f"Average Grade: {average:.2f}\n"
            f"Final Grade: {letter_grade}"
        )
        self.result_label.setText(result_text)

    def get_letter_grade(self, avg):
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


def main():
    app = QApplication(sys.argv)
    window = StudentGradingSystem()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
