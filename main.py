import sys
import webbrowser

from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6.QtCore import QThread
from PyQt6.QtGui import QMovie

from ui.test import Ui_MainWindow
from ui.filter import Ui_Dialog

from api.flights_finder import Picker

class FlightSearcher(QThread,Picker):

    def __init__(self, radius:str, location:str):
        super().__init__()
        self.__radius = radius
        self.__location = location

    def run(self) -> list:
        results = self.get_by_bounds(self.__radius, self.__location)
        print(f"Search results: {results}")  # Debugging output


class OpenBrowserThread(QThread):
    #Runs webbrowser.open() in a separate thread to avoid PyQt  issues
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        webbrowser.open(self.url)  # Open link in default browser

class FilterDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Close the dialog when "Set up" button is clicked
        self.pushButton_setUp.clicked.connect(self.accept)

    def keyPressEvent(self, event):
        if event.key() == 16777220:  # Enter key
            self.accept()

class FlightTracker(QMainWindow):
    def __init__(self):
        super(FlightTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.filterDialog = FilterDialog()

        #Ensure that the label is visible and the table is not
        self.ui.label.setVisible(True)
        self.ui.flightsTable.setVisible(False)

        # Store the thread instance as an attribute to prevent garbage collection
        self.browser_thread = None
        self.finder_thread = None

        # Button clicks calls 
        self.ui.pushButton_configureFilters.clicked.connect(self.openFilterDialog)
        self.ui.pushButton_flightRadar.clicked.connect(lambda: self._goto("https://www.flightradar24.com"))
        self.ui.pushButton_googleMaps.clicked.connect(lambda: self._goto("https://www.google.pl/maps"))
        self.ui.pushButton_search.clicked.connect(lambda: self._searchForFlights())

    
    def _goto(self, url: str) -> None:
        self.browser_thread = OpenBrowserThread(url)
        self.browser_thread.start()  # Start the thread safely


    def _searchForFlights(self):
        self.movie = QMovie("./src/__Iphone-spinner-1.gif")
        self.ui.label.setMovie(self.movie)
        self.movie.start()

        self.finder_thread = FlightSearcher(100,"Wrocław")
        self.finder_thread.start()


    def openFilterDialog(self):
        self.filterDialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlightTracker()
    window.show()
    sys.exit(app.exec())
