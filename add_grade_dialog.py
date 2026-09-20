from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class AddGradeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Grade")
        self.setFixedSize(400, 320)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)

        self.student_id = ""
        self.grade = 0.0

        self.setup_ui()
        self.apply_style()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(15)

        title_label = QLabel("Record Student Grade")
        title_label.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Student ID Field
        lbl_id = QLabel("Student ID:")
        lbl_id.setFont(QFont("Segoe UI", 10, QFont.Weight.DemiBold))
        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("Enter registered Student ID")
        layout.addWidget(lbl_id)
        layout.addWidget(self.input_id)

        # Grade Field
        lbl_grade = QLabel("Numeric Grade:")
        lbl_grade.setFont(QFont("Segoe UI", 10, QFont.Weight.DemiBold))
        self.input_grade = QLineEdit()
        self.input_grade.setPlaceholderText("e.g. 88.5 or 95")
        layout.addWidget(lbl_grade)
        layout.addWidget(self.input_grade)

        layout.addSpacing(10)

        # Action Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)

        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.clicked.connect(self.reject)

        self.btn_save = QPushButton("Submit Grade")
        self.btn_save.setObjectName("primaryButton")
        self.btn_save.clicked.connect(self.validate_and_accept)

        btn_layout.addWidget(self.btn_cancel)
        btn_layout.addWidget(self.btn_save)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def validate_and_accept(self):
        s_id = self.input_id.text().strip()
        g_str = self.input_grade.text().strip()

        if not s_id or not g_str:
            QMessageBox.warning(self, "Validation Error", "All fields are required!")
            return

        try:
            val = float(g_str)
            if val < 0 or val > 100:
                QMessageBox.warning(self, "Validation Error", "Grade must be between 0 and 100.")
                return
            self.grade = val
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid numeric grade.")
            return

        self.student_id = s_id
        self.accept()

    def get_data(self):
        return self.student_id, self.grade

    def apply_style(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #ffffff;
                border: 2px solid #004080;
                border-radius: 12px;
            }
            QLabel {
                color: #004080;
            }
            QLineEdit {
                border: 1.5px solid #dcdfe6;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 13px;
                background-color: #f9faec;
                color: #2c3e50;
            }
            QLineEdit:focus {
                border: 1.5px solid #004080;
                background-color: #ffffff;
            }
            QPushButton {
                padding: 10px 16px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 13px;
                background-color: #e4e7ed;
                color: #606266;
                border: none;
            }
            QPushButton:hover {
                background-color: #dcdfe6;
            }
            QPushButton#primaryButton {
                background-color: #004080;
                color: white;
            }
            QPushButton#primaryButton:hover {
                background-color: #0056b3;
            }
        """)