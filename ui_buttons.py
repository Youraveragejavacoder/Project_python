from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QStackedWidget, QMessageBox,
    QSizeGrip, QHBoxLayout, QFrame, QPushButton, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QFont, QColor, QCursor
from PyQt6.QtCore import Qt, QPoint

from logic import GradeManager
from auth_widgets import SignupWidget, LoginWidget
from title_bar import CustomTitleBar
from add_student_dialog import AddStudentDialog
from add_grade_dialog import AddGradeDialog
from view_average_dialog import ViewAverageDialog


class GradingSystemUI(QWidget):
    MARGIN = 8  # Detection margin in pixels for border dragging

    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Student Grading System")
        self.resize(950, 700)
        self.setMinimumSize(800, 600)  # Ensures resizing has limits

        # Enable mouse tracking to detect window edges for resizing
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self._resizing = False
        self._resize_edge = None
        self._drag_pos = QPoint()

        self.db = db
        self.grade_manager = GradeManager(db)

        self.stack = QStackedWidget()
        self.login_widget = LoginWidget(self.handle_login, self.show_signup)
        self.signup_widget = SignupWidget(self.handle_signup)
        self.signup_widget.back_login_button.clicked.connect(self.show_login)

        self.main_widget = QWidget()
        self.setup_main_ui()

        self.stack.addWidget(self.login_widget)
        self.stack.addWidget(self.signup_widget)
        self.stack.addWidget(self.main_widget)

        root_layout = QVBoxLayout()
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        self.title_bar = CustomTitleBar(self, "Student Grading System")
        root_layout.addWidget(self.title_bar)
        root_layout.addWidget(self.stack)

        self.setLayout(root_layout)
        self.apply_theme()

        self.size_grip = QSizeGrip(self)
        self.size_grip.setFixedSize(20, 20)
        self.stack.setCurrentWidget(self.login_widget)

    # --- Edge Resize Mouse Handlers ---
    def mouseMoveEvent(self, event):
        pos = event.position().toPoint()

        if self._resizing:
            rect = self.geometry()
            global_pos = event.globalPosition().toPoint()

            if 'right' in self._resize_edge:
                rect.setRight(global_pos.x())
            if 'bottom' in self._resize_edge:
                rect.setBottom(global_pos.y())
            if 'left' in self._resize_edge:
                rect.setLeft(global_pos.x())
            if 'top' in self._resize_edge:
                rect.setTop(global_pos.y())

            if rect.width() >= self.minimumWidth() and rect.height() >= self.minimumHeight():
                self.setGeometry(rect)
            return

        # Update cursor shape based on edge proximity
        edge = self._get_edge(pos)
        if edge in ('top-left', 'bottom-right'):
            self.setCursor(QCursor(Qt.CursorShape.SizeFDiagCursor))
        elif edge in ('top-right', 'bottom-left'):
            self.setCursor(QCursor(Qt.CursorShape.SizeBDiagCursor))
        elif edge in ('left', 'right'):
            self.setCursor(QCursor(Qt.CursorShape.SizeHorCursor))
        elif edge in ('top', 'bottom'):
            self.setCursor(QCursor(Qt.CursorShape.SizeVerCursor))
        else:
            self.unsetCursor()

        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            edge = self._get_edge(event.position().toPoint())
            if edge:
                self._resizing = True
                self._resize_edge = edge
                self._drag_pos = event.globalPosition().toPoint()
                return
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self._resizing = False
        self._resize_edge = None
        self.unsetCursor()
        super().mouseReleaseEvent(event)

    def _get_edge(self, pos):
        w, h = self.width(), self.height()
        m = self.MARGIN

        top = pos.y() <= m
        bottom = pos.y() >= h - m
        left = pos.x() <= m
        right = pos.x() >= w - m

        if top and left: return 'top-left'
        if top and right: return 'top-right'
        if bottom and left: return 'bottom-left'
        if bottom and right: return 'bottom-right'
        if top: return 'top'
        if bottom: return 'bottom'
        if left: return 'left'
        if right: return 'right'
        return None

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.size_grip.move(self.width() - 20, self.height() - 20)
        self.size_grip.raise_()

    # --- Standard App Methods ---
    def apply_theme(self):
        self.setStyleSheet("QWidget { background-color: #f0f4f8; font-family: 'Segoe UI', sans-serif; }")

    def show_signup(self):
        self.stack.setCurrentWidget(self.signup_widget)

    def show_login(self):
        self.stack.setCurrentWidget(self.login_widget)

    def show_main_screen(self):
        self.stack.setCurrentWidget(self.main_widget)

    def handle_signup(self, user_id, password):
        if self.db.user_exists(user_id):
            QMessageBox.warning(self, "Signup Error", "ID number already registered!")
            return False
        self.db.add_user(user_id, password)
        return True

    def handle_login(self, user_id, password):
        if self.db.validate_user(user_id, password):
            self.show_main_screen()
            return True
        return False

    def setup_main_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 20, 40, 40)

        header = QLabel("Dashboard")
        header.setFont(QFont("Segoe UI", 28, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("color: #1e293b; margin-bottom: 10px;")
        layout.addWidget(header)

        card_frame = QFrame()
        card_frame.setStyleSheet(
            "QFrame { background-color: #ffffff; border-radius: 16px; border: 1px solid #e2e8f0; }")

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setColor(QColor(0, 0, 0, 25))
        shadow.setOffset(0, 8)
        card_frame.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout(card_frame)
        card_layout.setContentsMargins(50, 50, 50, 50)
        card_layout.setSpacing(35)

        btn_add_student = self.create_menu_button("👨‍🎓 Add New Student",
                                                  "Register a new student ID and name into the system.")
        btn_add_student.clicked.connect(self.add_student_dialog)

        btn_add_grade = self.create_menu_button("📝 Record Grade", "Input a new numeric grade for an existing student.")
        btn_add_grade.clicked.connect(self.add_grade_dialog)

        btn_view_avg = self.create_menu_button("📊 View Average",
                                               "Calculate and display the overall average grade for a student.")
        btn_view_avg.clicked.connect(self.view_average_dialog)

        card_layout.addWidget(btn_add_student)
        card_layout.addWidget(btn_add_grade)
        card_layout.addWidget(btn_view_avg)

        layout.addStretch()
        card_h_layout = QHBoxLayout()
        card_h_layout.addStretch()
        card_h_layout.addWidget(card_frame, stretch=2)
        card_h_layout.addStretch()
        layout.addLayout(card_h_layout)
        layout.addStretch()

        self.main_widget.setLayout(layout)

    def create_menu_button(self, title, subtitle):
        btn = QPushButton(f"{title}\n{subtitle}")
        btn.setStyleSheet("""
            QPushButton {
                text-align: left; padding: 20px 25px;
                background-color: #f8fafc; border: 2px solid #e2e8f0;
                border-radius: 12px; color: #0f172a; font-size: 16px; font-weight: bold;
            }
            QPushButton:hover { background-color: #f0fdf4; border: 2px solid #22c55e; color: #166534; }
            QPushButton:pressed { background-color: #dcfce7; }
        """)
        return btn

    def open_dialog_with_hidden_bg(self, dialog_class, *args):
        self.main_widget.setVisible(False)
        dialog = dialog_class(*args, parent=self)
        result = dialog.exec()
        self.main_widget.setVisible(True)
        return result, dialog

    def add_student_dialog(self):
        result, dialog = self.open_dialog_with_hidden_bg(AddStudentDialog)
        if result == AddStudentDialog.DialogCode.Accepted:
            student_id, name = dialog.get_data()
            self.grade_manager.add_student(student_id, name)
            QMessageBox.information(self, "Success", f"Student '{name}' ({student_id}) added successfully!")

    def add_grade_dialog(self):
        result, dialog = self.open_dialog_with_hidden_bg(AddGradeDialog)
        if result == AddGradeDialog.DialogCode.Accepted:
            student_id, grade = dialog.get_data()
            self.grade_manager.add_grade(student_id, grade)
            QMessageBox.information(self, "Success", f"Grade {grade} registered for Student #{student_id}!")

    def view_average_dialog(self):
        self.open_dialog_with_hidden_bg(ViewAverageDialog, self.grade_manager)