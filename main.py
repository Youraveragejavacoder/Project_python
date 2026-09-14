from PyQt6.QtWidgets import QApplication
from ui import GradingSystemUI
from database import Database

def main():
    app = QApplication([])
    db = Database()
    ui = GradingSystemUI(db)
    ui.showFullScreen()
    app.exec()

if __name__ == "__main__":
    main()
