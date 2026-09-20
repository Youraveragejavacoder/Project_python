from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class SignupWidget(QWidget):
    def __init__(self, on_signup_success):
        super().__init__()
        self.on_signup_success = on_signup_success
        self.setWindowTitle("Sign Up")

        layout = QVBoxLayout()
        layout.setContentsMargins(100, 60, 100, 60)
        layout.setSpacing(18)
        self.setLayout(layout)

        title = QLabel("Sign Up")
        title.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: black;")
        layout.addWidget(title)

        self.id_label = QLabel("ID Number:")
        self.id_label.setFont(QFont("Segoe UI", 14))
        self.id_label.setStyleSheet("color: black;")
        layout.addWidget(self.id_label)

        self.id_input = QLineEdit()
        self.id_input.setFont(QFont("Segoe UI", 12))
        self.id_input.setPlaceholderText("Enter your ID number")
        self.id_input.setStyleSheet("""
            padding:8px;
            border: 2px solid #007acc;
            border-radius: 6px;
            color: black;
            background-color: #dbe9ff;
        """)
        layout.addWidget(self.id_input)

        self.pass_label = QLabel("Password:")
        self.pass_label.setFont(QFont("Segoe UI", 14))
        self.pass_label.setStyleSheet("color: black;")
        layout.addWidget(self.pass_label)

        self.pass_input = QLineEdit()
        self.pass_input.setFont(QFont("Segoe UI", 12))
        self.pass_input.setPlaceholderText("Create a password")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_input.setStyleSheet("""
            padding:8px;
            border: 2px solid #007acc;
            border-radius: 6px;
            color: black;
            background-color: #dbe9ff;
        """)
        layout.addWidget(self.pass_input)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        self.signup_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.signup_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #007acc, stop:1 #00bfff);
                border-radius: 10px;
                color: white;
                padding: 12px;
            }
            QPushButton:hover {
                background: #005f9e;
            }
            QPushButton:pressed {
                background-color: #004c7f;
            }
        """)
        self.signup_button.clicked.connect(self.handle_signup)
        layout.addWidget(self.signup_button)

        self.back_login_button = QPushButton("Back to Login")
        self.back_login_button.setFont(QFont("Segoe UI", 12))
        self.back_login_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.back_login_button.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: #007acc;
                text-decoration: underline;
                border: none;
                margin-top: 10px;
            }
            QPushButton:hover {
                color: #005f9e;
            }
        """)
        layout.addWidget(self.back_login_button)

    def handle_signup(self):
        user_id = self.id_input.text().strip()
        password = self.pass_input.text().strip()

        if not user_id or not password:
            QMessageBox.warning(self, "Empty Fields", "Please enter both ID number and password.")
            return

        if self.on_signup_success(user_id, password):
            QMessageBox.information(self, "Success", "You have signed up successfully! Please log in.")
            self.id_input.clear()
            self.pass_input.clear()


class LoginWidget(QWidget):
    def __init__(self, on_login_success, on_request_signup):
        super().__init__()
        self.on_login_success = on_login_success
        self.on_request_signup = on_request_signup
        self.setWindowTitle("Login")

        layout = QVBoxLayout()
        layout.setContentsMargins(100, 60, 100, 60)
        layout.setSpacing(18)
        self.setLayout(layout)

        title = QLabel("Login")
        title.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: black;")
        layout.addWidget(title)

        self.id_label = QLabel("ID Number:")
        self.id_label.setFont(QFont("Segoe UI", 14))
        self.id_label.setStyleSheet("color: black;")
        layout.addWidget(self.id_label)

        self.id_input = QLineEdit()
        self.id_input.setFont(QFont("Segoe UI", 12))
        self.id_input.setPlaceholderText("Enter your ID number")
        self.id_input.setStyleSheet("""
            padding:8px;
            border: 2px solid #007acc;
            border-radius: 6px;
            color: black;
            background-color: #dbe9ff;
        """)
        layout.addWidget(self.id_input)

        self.pass_label = QLabel("Password:")
        self.pass_label.setFont(QFont("Segoe UI", 14))
        self.pass_label.setStyleSheet("color: black;")
        layout.addWidget(self.pass_label)

        self.pass_input = QLineEdit()
        self.pass_input.setFont(QFont("Segoe UI", 12))
        self.pass_input.setPlaceholderText("Enter your password")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_input.setStyleSheet("""
            padding:8px;
            border: 2px solid #007acc;
            border-radius: 6px;
            color: black;
            background-color: #dbe9ff;
        """)
        layout.addWidget(self.pass_input)

        self.login_button = QPushButton("Login")
        self.login_button.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        self.login_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #007acc, stop:1 #00bfff);
                border-radius: 10px;
                color: white;
                padding: 12px;
            }
            QPushButton:hover {
                background: #005f9e;
            }
            QPushButton:pressed {
                background-color: #004c7f;
            }
        """)
        self.login_button.clicked.connect(self.check_login)
        layout.addWidget(self.login_button)

        self.signup_request_button = QPushButton("Create an account")
        self.signup_request_button.setFont(QFont("Segoe UI", 12))
        self.signup_request_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.signup_request_button.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: #007acc;
                text-decoration: underline;
                border: none;
                margin-top: 10px;
            }
            QPushButton:hover {
                color: #005f9e;
            }
        """)
        self.signup_request_button.clicked.connect(self.on_request_signup)
        layout.addWidget(self.signup_request_button)

    def check_login(self):
        user_id = self.id_input.text().strip()
        password = self.pass_input.text().strip()

        if not user_id or not password:
            QMessageBox.warning(self, "Empty Fields", "Please enter your ID number and password.")
            return

        if self.on_login_success(user_id, password):
            self.id_input.clear()
            self.pass_input.clear()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid ID number or password.")
