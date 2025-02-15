import sys
import webbrowser

from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal, QTimer
from PyQt6.QtGui import QMovie

from ui.test import Ui_MainWindow
from ui.filter import Ui_Dialog

from api.flights_finder import Picker

class FlightSearcher(QThread,Picker):
    finished = pyqtSignal(list)

    def __init__(self, radius:str, location:str, metric:str):
        super().__init__()
        self.__radius = radius
        self.__location = location
        self.__metric = metric

    def run(self):
        results = self.get_by_bounds(self.__radius, self.__location, self.__metric)
        self.finished.emit(results) # because the function runs as a thread, signals are used to retrive results in the main thread


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

        #set table header resize mode manually cause it is unavaliable in editor
        header = self.ui.flightsTable.horizontalHeader() 
        for column in range(self.ui.flightsTable.columnCount()):
            header.setSectionResizeMode(column,QHeaderView.ResizeMode.Stretch)


        # Store the thread instance as an attribute to prevent garbage collection
        self.browser_thread = None
        self.finder_thread = None

        # Button clicks calls 
        self.ui.pushButton_configureFilters.clicked.connect(self.openFilterDialog)
        self.ui.pushButton_flightRadar.clicked.connect(lambda: self._goto("https://www.flightradar24.com"))
        self.ui.pushButton_googleMaps.clicked.connect(lambda: self._goto("https://www.google.pl/maps"))
        self.ui.pushButton_search.clicked.connect(lambda: self._searchForFlights())

        #using signals to check if the checkbox state has been changed
        self.ui.checkBox_applyFilters.stateChanged.connect(self._filter_manager)

        self.__found_flights = None # global variable to store results 

    
    def _goto(self, url: str) -> None:
        self.browser_thread = OpenBrowserThread(url)
        self.browser_thread.start()  # Start the thread safely


    def _searchForFlights(self):
        try:
            #making sure that spinner will appear and table will not
            self.ui.label.setVisible(True)
            self.ui.flightsTable.setVisible(False)

            self.finder_thread = FlightSearcher(int(self.ui.radius_edit.text()),str(self.ui.location_edit.text()), self.ui.comboBox.currentText())
            self.finder_thread.finished.connect(self._display_results) # send data from the connected signal to this funcion
            self.finder_thread.start()

            self.movie = QMovie("./src/__Iphone-spinner-1.gif") # make it into more relative path (use os path or something idk)
            self.ui.label.setMovie(self.movie)
            self.movie.start()

        except ValueError:
            self.ui.label.setText("An error occured")
            self.show_error_message("Invalid radius, please check input.")
            

    def _display_results(self, results):
        
        if results:
            self.__found_flights = results
            self._populate_table(results)
        else:
            self.ui.label.setText("No flights found in the area")

    def _populate_table(self,results):

        #creating amonut of rows needed for the flights
        self.ui.flightsTable.setRowCount(len(results)) 

        for row_id, flight in enumerate(results):

            #setting the items of each row up
            callsign = QTableWidgetItem(flight['callsing'])

            line = QTableWidgetItem(flight['icao'])
            line.setToolTip(flight['line'])

            model = QTableWidgetItem(flight['model'])

            departure = QTableWidgetItem(flight['departure_icao'])
            departure.setToolTip(flight['departure_name'])

            departure_time = QTableWidgetItem(flight['time_departure'])

            arrival = QTableWidgetItem(flight['arrival_icao'])
            arrival.setToolTip(flight['arrival_name'])

            arrival_time = QTableWidgetItem(flight['time_arrival'])

            #populating the row
            self.ui.flightsTable.setItem(row_id, 0, callsign)
            self.ui.flightsTable.setItem(row_id, 1, line)
            self.ui.flightsTable.setItem(row_id, 2, model)
            self.ui.flightsTable.setItem(row_id, 3, departure)
            self.ui.flightsTable.setItem(row_id, 4, departure_time)
            self.ui.flightsTable.setItem(row_id, 5, arrival)
            self.ui.flightsTable.setItem(row_id, 6, arrival_time)

        self.ui.label.setVisible(False)
        self.ui.flightsTable.setVisible(True)

    def _filter_manager(self):
        if self.ui.checkBox_applyFilters.isChecked() and self.__found_flights:
            print("is in checked state and there are flights to work with")
            if self.__found_flights:
                test = []
                parameters = ["callsign", "airline", "model", "departure", "departure_time", "arrival", "arrival_time"]
                for parameter in parameters:
                    line_edit = getattr(self.filterDialog, f"line_{parameter}", None)  # Dynamically get QLineEdit
                    if line_edit:  # Ensure QLineEdit exists
                        test.append(line_edit.text().strip())  # Get text from QLineEdit
                    else:
                        test.append("")  # Default value if QLineEdit not found
                print(test)
        elif self.ui.checkBox_applyFilters.isChecked() and not self.__found_flights:
                print("checked state but there are no flights, error")
                self.ui.checkBox_applyFilters.blockSignals(True)  # ❌ Temporarily stop signals
                self.show_error_message("No flights were detected")
                QTimer.singleShot(100, lambda: self.ui.checkBox_applyFilters.setChecked(False))# ✅ Uncheck the checkbox
                self.ui.checkBox_applyFilters.blockSignals(False)
        else:
            if self.__found_flights:
                print("unchecked, repopulating")
                self._populate_table(self.__found_flights) # if apply filter is unchecked, then repopulate table NO NEW SEARCH IS CONDUCTED
            else:
                print("unchecked but no flights, stopping")
                pass
        

    # Simple error message with the specified text
    def show_error_message(self, message): 
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Icon.Critical) 
        error_dialog.setWindowTitle("Error") 
        error_dialog.setText(message)  # Set error message
        error_dialog.exec()  # Show the dialog


    def openFilterDialog(self):
        self.filterDialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlightTracker()
    window.show()
    sys.exit(app.exec())
