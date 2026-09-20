from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import re


class AddStudentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Student")
        self.setFixedSize(400, 320)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog
        )

        self.student_id = ""
        self.student_name = ""

        # Student ID format: YYYY-XXXX
        self.student_pattern = re.compile(r"^\d{4}-\d{4}$")

        self.setup_ui()
        self.apply_style()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(15)

        # Header Title
        title_label = QLabel("Add New Student")
        title_label.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Student ID Field
        lbl_id = QLabel("Student ID:")
        lbl_id.setFont(QFont("Segoe UI", 10, QFont.Weight.DemiBold))

        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("e.g. 2026-0001")

        layout.addWidget(lbl_id)
        layout.addWidget(self.input_id)

        # Student Name Field
        lbl_name = QLabel("Full Name:")
        lbl_name.setFont(QFont("Segoe UI", 10, QFont.Weight.DemiBold))

        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("e.g. Jane Doe")

        layout.addWidget(lbl_name)
        layout.addWidget(self.input_name)

        layout.addSpacing(10)

        # Action Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)

        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.clicked.connect(self.reject)

        self.btn_save = QPushButton("Add Student")
        self.btn_save.setObjectName("primaryButton")
        self.btn_save.clicked.connect(self.validate_and_accept)

        btn_layout.addWidget(self.btn_cancel)
        btn_layout.addWidget(self.btn_save)

        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def validate_and_accept(self):
        s_id = self.input_id.text().strip()
        s_name = self.input_name.text().strip()

        # Check if fields are empty
        if not s_id or not s_name:
            QMessageBox.warning(
                self,
                "Validation Error",
                "All fields are required!"
            )
            return

        # Check Student ID format
        if not self.student_pattern.fullmatch(s_id):
            QMessageBox.warning(
                self,
                "Validation Error",
                "Student ID is invalid!\nFormat must be YYYY-XXXX."
            )
            return

        # Save the data only after validation succeeds
        self.student_id = s_id
        self.student_name = s_name

        # Close dialog successfully
        self.accept()

    def get_data(self):
        return self.student_id, self.student_name

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