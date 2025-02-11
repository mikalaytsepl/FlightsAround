import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "ui", "test.ui")
        uic.loadUi(ui_path, self)  # Wczytanie UI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
