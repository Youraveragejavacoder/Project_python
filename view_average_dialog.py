from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class ViewAverageDialog(QDialog):
    def __init__(self, grade_manager, parent=None):
        super().__init__(parent)
        self.grade_manager = grade_manager
        self.setWindowTitle("View Student Average")
        self.setFixedSize(420, 360)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)

        self.setup_ui()
        self.apply_style()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(12)

        title_label = QLabel("Calculate Grade Average")
        title_label.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Input Row
        lbl_id = QLabel("Enter Student ID:")
        lbl_id.setFont(QFont("Segoe UI", 10, QFont.Weight.DemiBold))
        layout.addWidget(lbl_id)

        search_layout = QHBoxLayout()
        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("Student ID...")

        self.btn_fetch = QPushButton("Lookup")
        self.btn_fetch.setObjectName("primaryButton")
        self.btn_fetch.clicked.connect(self.calculate_average)

        search_layout.addWidget(self.input_id)
        search_layout.addWidget(self.btn_fetch)
        layout.addLayout(search_layout)

        # Visual Result Card
        self.result_card = QFrame()
        self.result_card.setObjectName("resultCard")
        card_layout = QVBoxLayout()
        card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.status_label = QLabel("Enter ID to query overall average")
        self.status_label.setFont(QFont("Segoe UI", 10))
        self.status_label.setStyleSheet("color: #7f8c8d;")

        self.avg_display = QLabel("--")
        self.avg_display.setFont(QFont("Segoe UI", 36, QFont.Weight.Bold))
        self.avg_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.avg_display.setStyleSheet("color: #004080;")

        card_layout.addWidget(self.status_label)
        card_layout.addWidget(self.avg_display)
        self.result_card.setLayout(card_layout)
        layout.addWidget(self.result_card)

        # Bottom Close Button
        self.btn_close = QPushButton("Done")
        self.btn_close.clicked.connect(self.accept)
        layout.addWidget(self.btn_close)

        self.setLayout(layout)

    def calculate_average(self):
        s_id = self.input_id.text().strip()
        if not s_id:
            self.status_label.setText("Please specify a Student ID")
            self.avg_display.setText("--")
            return

        avg = self.grade_manager.get_average_grade(s_id)
        if avg > 0:
            self.status_label.setText(f"Average for Student #{s_id}:")
            self.avg_display.setText(f"{avg:.2f}")
        else:
            self.status_label.setText("No grades found for this ID")
            self.avg_display.setText("N/A")

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
            QFrame#resultCard {
                background-color: #f5f7fb;
                border: 1px dashed #cbd5e1;
                border-radius: 10px;
                margin-top: 5px;
                margin-bottom: 5px;
            }
            QPushButton {
                padding: 9px 16px;
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