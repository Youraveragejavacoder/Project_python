from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit,
    QStackedWidget, QMessageBox, QHBoxLayout
)
from PyQt6.QtGui import QFont, QColor, QPalette, QBrush, QLinearGradient
from PyQt6.QtCore import Qt
from logic import GradeManager

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
        title.setStyleSheet("color: black;")  # black text for visibility
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

        # Call the logic to add user credentials
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

class GradingSystemUI(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Student Grading System")
        self.resize(900, 600)
        self.db = db
        self.grade_manager = GradeManager(db)

        self.stack = QStackedWidget()

        # Create login & signup widgets, pass callbacks
        self.login_widget = LoginWidget(self.handle_login, self.show_signup)
        self.signup_widget = SignupWidget(self.handle_signup)

        # Connect 'back to login' button from signup_widget
        self.signup_widget.back_login_button.clicked.connect(self.show_login)

        self.main_widget = QWidget()
        self.setup_main_ui()

        self.stack.addWidget(self.login_widget)   # index 0
        self.stack.addWidget(self.signup_widget)  # index 1
        self.stack.addWidget(self.main_widget)    # index 2

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

        self.apply_style()
        self.stack.setCurrentWidget(self.login_widget)

    def apply_style(self):
        # Light background with subtle gradient for clarity
        palette = QPalette()
        palette.setColor(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, QColor("#f5f7fb"))
        palette.setColor(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, QColor("#f5f7fb"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    # UI page switches
    def show_signup(self):
        self.stack.setCurrentWidget(self.signup_widget)

    def show_login(self):
        self.stack.setCurrentWidget(self.login_widget)

    def show_main_screen(self):
        self.stack.setCurrentWidget(self.main_widget)

    # Authentication handling using the database for login/signup
    def handle_signup(self, user_id, password):
        # Check if user exists already
        if self.db.user_exists(user_id):
            QMessageBox.warning(self, "Signup Error", "ID number already registered!")
            return False
        # Add user
        self.db.add_user(user_id, password)
        return True

    def handle_login(self, user_id, password):
        if self.db.validate_user(user_id, password):
            self.show_main_screen()
            return True
        return False

    def setup_main_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(30)
        self.main_widget.setLayout(layout)

        title = QLabel("Student Grading System")
        title.setFont(QFont("Segoe UI", 36, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            color: #004080;
        """)
        layout.addWidget(title)

        button_style = """
            QPushButton {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #007acc, stop:1 #00bfff);
                border-radius: 12px;
                color: white;
                padding: 18px;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: #005f9e;
            }
            QPushButton:pressed {
                background-color: #004c7f;
            }
        """

        add_student_btn = QPushButton("Add Student")
        add_student_btn.setStyleSheet(button_style)
        add_student_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        add_student_btn.clicked.connect(self.add_student_dialog)
        layout.addWidget(add_student_btn)

        add_grade_btn = QPushButton("Add Grade")
        add_grade_btn.setStyleSheet(button_style)
        add_grade_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        add_grade_btn.clicked.connect(self.add_grade_dialog)
        layout.addWidget(add_grade_btn)

        view_avg_btn = QPushButton("View Average Grade")
        view_avg_btn.setStyleSheet(button_style)
        view_avg_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        view_avg_btn.clicked.connect(self.view_average_dialog)
        layout.addWidget(view_avg_btn)

        layout.addStretch()

    def add_student_dialog(self):
        from PyQt6.QtWidgets import QInputDialog
        student_id, ok1 = QInputDialog.getText(self, "Add Student", "Student ID:")
        if not ok1 or not student_id.strip():
            return
        name, ok2 = QInputDialog.getText(self, "Add Student", "Student Name:")
        if ok2 and name.strip():
            self.grade_manager.add_student(student_id.strip(), name.strip())
            QMessageBox.information(self, "Success", f"Added student {name.strip()} ({student_id.strip()})")

    def add_grade_dialog(self):
        from PyQt6.QtWidgets import QInputDialog
        student_id, ok1 = QInputDialog.getText(self, "Add Grade", "Student ID:")
        if not ok1 or not student_id.strip():
            return
        grade_str, ok2 = QInputDialog.getText(self, "Add Grade", "Grade (0-100):")
        if ok2 and grade_str.strip():
            try:
                grade = float(grade_str.strip())
                if 0 <= grade <= 100:
                    self.grade_manager.add_grade(student_id.strip(), grade)
                    QMessageBox.information(self, "Success", f"Added grade {grade} to student {student_id.strip()}")
                else:
                    QMessageBox.warning(self, "Invalid Grade", "Grade must be between 0 and 100")
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", "Please enter a numeric grade")

    def view_average_dialog(self):
        from PyQt6.QtWidgets import QInputDialog
        student_id, ok = QInputDialog.getText(self, "View Average Grade", "Student ID:")
        if ok and student_id.strip():
            average = self.grade_manager.get_average_grade(student_id.strip())
            QMessageBox.information(self, "Average Grade", f"Student {student_id.strip()} average grade: {average:.2f}")
