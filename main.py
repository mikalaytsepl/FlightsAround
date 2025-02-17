import sys
import os
import webbrowser
import pandas as pd

from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QHeaderView, QTableWidgetItem, QMessageBox, QFileDialog
from PyQt6.QtCore import QThread, pyqtSignal, QTimer
from PyQt6.QtGui import QMovie

from ui.main_ui import Ui_MainWindow
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
        self.ui.pushButton_configureFilters.clicked.connect(self._openFilterDialog)
        self.ui.pushButton_flightRadar.clicked.connect(lambda: self._goto("https://www.flightradar24.com"))
        self.ui.pushButton_googleMaps.clicked.connect(lambda: self._goto("https://www.google.pl/maps"))
        self.ui.pushButton_search.clicked.connect(lambda: self._searchForFlights())
        self.ui.pushButton_save.clicked.connect(lambda: self._save_table())

        #using signals to check if the checkbox state has been changed
        self.ui.checkBox_applyFilters.stateChanged.connect(self._filter_manager)

        self.__found_flights = None # global variable to store results 

    
    def _goto(self, url: str) -> None:
        self.browser_thread = OpenBrowserThread(url)
        self.browser_thread.start()  # Start the thread safely


    def _searchForFlights(self):
        try:
            if self.finder_thread and self.finder_thread.isRunning():
                return  # Prevent multiple searches if a thread is already running

            self.ui.pushButton_search.setEnabled(False) # disabling the search button so user will not click it multiple times

            #making sure that spinner will appear and table will not
            self.ui.label.setVisible(True)
            self.ui.flightsTable.setVisible(False)

            self.finder_thread = FlightSearcher(int(self.ui.radius_edit.text()),str(self.ui.location_edit.text()), self.ui.comboBox.currentText())
            self.finder_thread.finished.connect(self._display_results) # send data from the connected signal to this funcion
            self.finder_thread.start()

            # getting an absolute of the script and only then getting a path to a gif, allows to access it from everywhere
            # ps. not in init cause there's no need for it to be in global scope 
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            gif_path = os.path.join(BASE_DIR, "src", "output-onlinegiftools.gif")

            self.movie = QMovie(gif_path) # make it into more relative path (use os path or something idk)
            self.ui.label.setMovie(self.movie)
            self.movie.start()

        except ValueError:
            self.ui.label.setText("An error occured")
            self._show_message("Invalid radius, please check input.")
            self.ui.pushButton_search.setEnabled(True)  # re enable button in case of problems
            

    def _display_results(self, results):
        if results:
            self.__found_flights = results
            self._populate_table(results)
        else:
            self.__found_flights = None # if there's no flights, ensure that old ones will not appear in filters
            self.ui.label.setText("No flights found in the area")
        self.ui.pushButton_search.setEnabled(True) # when search is over, enable button 

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
            if self.__found_flights:
                filter_params = {}

                # static calling whould be faster, but this approach is more scallable 
                for parameter in range(self.ui.flightsTable.columnCount()):
                    line_edit = getattr(self.filterDialog, f"line_{parameter}", None)  # Dynamically get QLineEdit
                    if line_edit and line_edit.text().strip() :  # Ensure QLineEdit exists and is not empty
                        filter_params[parameter] = line_edit.text().strip() # Get text from QLineEdit

            # no unnecessary checks will be conducted if there are no filter parameters set 
            if not filter_params:
                return

            rows_to_remove=[]
            for row in range(self.ui.flightsTable.rowCount()):  
                row_data = [
                        self.ui.flightsTable.item(row, col).text() if self.ui.flightsTable.item(row, col) else ""
                        for col in range(self.ui.flightsTable.columnCount())]
                #old version
                """for col in range(self.ui.flightsTable.columnCount()): 
                    item = self.ui.flightsTable.item(row, col)  # Get QTableWidgetItem
                    row_data.append(item.text() if item else "")  # Store text (or empty if None)"""
                    
                if not all(row_data[pos] == value for pos, value in filter_params.items()):
                    rows_to_remove.append(row)
                
            # this trick allows to delete rows without shifting others because we are removing from the end 
            for row in reversed(rows_to_remove):
                self.ui.flightsTable.removeRow(row)
                       


        elif self.ui.checkBox_applyFilters.isChecked() and not self.__found_flights:
                self.ui.checkBox_applyFilters.blockSignals(True)  # ❌ Temporarily stop signals
                self._show_message("No flights were detected")
                QTimer.singleShot(100, lambda: self.ui.checkBox_applyFilters.setChecked(False))# ✅ Uncheck the checkbox
                self.ui.checkBox_applyFilters.blockSignals(False)
        else:
            if self.__found_flights:
                self._populate_table(self.__found_flights) # if apply filter is unchecked, then repopulate table NO NEW SEARCH IS CONDUCTED
            else:
                pass



    def _save_table(self):
        #showing a message if there's no flights in the table (search results do not matter)
        # cause there might be incorrect filter for them 
        if not self.ui.flightsTable.rowCount():
            self._show_message("There is nothing to save yet")
            return None 

        # standard "saving vindow"
        file_name, _ = QFileDialog.getSaveFileName(
        self,
        "Save Table",
        "",
        "Excel Files (*.xlsx);;All Files (*)"
        )

        
        if file_name:
            if not file_name.endswith(".xlsx"):  # Ensure correct file extension
                file_name += ".xlsx"

            # extracting headers from the table 
            headers = [self.ui.flightsTable.horizontalHeaderItem(col).text() for col in range(self.ui.flightsTable.columnCount())]

            # Extract rows
            table_data = []
            for row in range(self.ui.flightsTable.rowCount()):
                row_data = [
                    self.ui.flightsTable.item(row, col).text() if self.ui.flightsTable.item(row, col) else ""
                    for col in range(self.ui.flightsTable.columnCount())
                ]
                table_data.append(row_data)

            # Convert to DataFrame
            df = pd.DataFrame(table_data, columns=headers)

            # save to Excel and show the popup with path afterwards
            df.to_excel(file_name, index=False, engine='openpyxl')
            self._show_message(f"Table saved to {file_name}","Information")

                


    # Simple error message with the specified text and symbol (critical byt default)
    def _show_message(self, message, symbol="Critical"): 
        if symbol not in ("Critical", "Warning", "Information", "Question"):
            symbol = "Critical" # fallback to default symbol in case if function is called with invalid argument
        error_dialog = QMessageBox()
        error_dialog.setIcon(getattr(QMessageBox.Icon, symbol)) 
        error_dialog.setWindowTitle(symbol) 
        error_dialog.setText(message)  # Set error message
        error_dialog.exec()  # Show the dialog


    def _openFilterDialog(self):
        self.filterDialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlightTracker()
    window.show()
    sys.exit(app.exec())
