from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class CustomTitleBar(QWidget):
    def __init__(self, parent=None, title_text=""):
        super().__init__(parent)
        self.parent_window = parent
        self.setFixedHeight(45)
        self.initial_pos = None

        layout = QHBoxLayout()
        layout.setContentsMargins(15, 0, 8, 0)
        layout.setSpacing(8)

        # Title Label
        self.title_label = QLabel(title_text)
        self.title_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: #004080; letter-spacing: 1px;")
        layout.addWidget(self.title_label)

        layout.addStretch()

        # Highly Visible Window Control Buttons
        self.btn_minimize = QPushButton("🗕")
        self.btn_maximize = QPushButton("🗖")
        self.btn_close = QPushButton("✕")

        for btn in (self.btn_minimize, self.btn_maximize, self.btn_close):
            btn.setFixedSize(35, 30)
            layout.addWidget(btn)

        self.setLayout(layout)
        self.apply_style()

        # Connections
        self.btn_minimize.clicked.connect(self.minimize_window)
        self.btn_maximize.clicked.connect(self.toggle_maximize)
        self.btn_close.clicked.connect(self.close_window)

    # --- Allow Dragging the Frameless Window ---
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.initial_pos = event.position().toPoint()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.initial_pos is not None and self.parent_window:
            delta = event.position().toPoint() - self.initial_pos
            self.parent_window.move(self.parent_window.pos() + delta)
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.initial_pos = None
        super().mouseReleaseEvent(event)

    # --- Window Controls ---
    def minimize_window(self):
        if self.parent_window:
            self.parent_window.showMinimized()

    def toggle_maximize(self):
        if self.parent_window:
            if self.parent_window.isMaximized():
                self.parent_window.showNormal()
                self.btn_maximize.setText("🗖")
            else:
                self.parent_window.showMaximized()
                self.btn_maximize.setText("🗗")

    def close_window(self):
        if self.parent_window:
            self.parent_window.close()

    def apply_style(self):
        # Buttons now have a default background color (e.g., #e2e8f0) to make them clearly visible
        self.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
            QPushButton {
                border: none;
                border-radius: 4px;
                background-color: #e2e8f0; 
                color: #334155;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #cbd5e1;
                color: #004080;
            }
            QPushButton:pressed {
                background-color: #94a3b8;
            }
            QPushButton:last-child {
                background-color: #fecaca;
                color: #b91c1c;
            }
            QPushButton:last-child:hover {
                background-color: #ef4444; 
                color: white;
            }
            QPushButton:last-child:pressed {
                background-color: #dc2626;
            }
        """)