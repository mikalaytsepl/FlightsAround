import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.test import Ui_MainWindow

class FlightTracker(QMainWindow):
    def __init__(self):
        super(FlightTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlightTracker()
    window.show()

    sys.exit(app.exec())