# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 632)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("weather-overcast")
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("background-color: rgb(44, 47, 51);\n"
"font: 10pt \"System-ui\";")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalWidget_2.setMaximumSize(QtCore.QSize(1000, 100))
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_flightRadar = QtWidgets.QPushButton(parent=self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_flightRadar.sizePolicy().hasHeightForWidth())
        self.pushButton_flightRadar.setSizePolicy(sizePolicy)
        self.pushButton_flightRadar.setStyleSheet("font: 10pt \"System-ui\";")
        self.pushButton_flightRadar.setObjectName("pushButton_flightRadar")
        self.verticalLayout.addWidget(self.pushButton_flightRadar)
        self.pushButton_googleMaps = QtWidgets.QPushButton(parent=self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_googleMaps.sizePolicy().hasHeightForWidth())
        self.pushButton_googleMaps.setSizePolicy(sizePolicy)
        self.pushButton_googleMaps.setStyleSheet("font: 10pt \"System-ui\";")
        self.pushButton_googleMaps.setObjectName("pushButton_googleMaps")
        self.verticalLayout.addWidget(self.pushButton_googleMaps)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_save = QtWidgets.QPushButton(parent=self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy)
        self.pushButton_save.setStyleSheet("font: 10pt \"System-ui\";")
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout_2.addWidget(self.pushButton_save)
        self.pushButton_configureFilters = QtWidgets.QPushButton(parent=self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_configureFilters.sizePolicy().hasHeightForWidth())
        self.pushButton_configureFilters.setSizePolicy(sizePolicy)
        self.pushButton_configureFilters.setStyleSheet("font: 10pt \"System-ui\";")
        self.pushButton_configureFilters.setObjectName("pushButton_configureFilters")
        self.verticalLayout_2.addWidget(self.pushButton_configureFilters)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.location_edit = QtWidgets.QLineEdit(parent=self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location_edit.sizePolicy().hasHeightForWidth())
        self.location_edit.setSizePolicy(sizePolicy)
        self.location_edit.setStyleSheet("font: 10pt \"System-ui\";\n"
"color: white")
        self.location_edit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText)
        self.location_edit.setObjectName("location_edit")
        self.verticalLayout_3.addWidget(self.location_edit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radius_edit = QtWidgets.QLineEdit(parent=self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radius_edit.sizePolicy().hasHeightForWidth())
        self.radius_edit.setSizePolicy(sizePolicy)
        self.radius_edit.setStyleSheet("font: 10pt \"System-ui\";\n"
"color: white")
        self.radius_edit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText)
        self.radius_edit.setObjectName("radius_edit")
        self.horizontalLayout_4.addWidget(self.radius_edit)
        self.comboBox = QtWidgets.QComboBox(parent=self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_search = QtWidgets.QPushButton(parent=self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_search.sizePolicy().hasHeightForWidth())
        self.pushButton_search.setSizePolicy(sizePolicy)
        self.pushButton_search.setStyleSheet("font: 10pt \"System-ui\";")
        self.pushButton_search.setObjectName("pushButton_search")
        self.verticalLayout_4.addWidget(self.pushButton_search)
        self.checkBox_applyFilters = QtWidgets.QCheckBox(parent=self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_applyFilters.sizePolicy().hasHeightForWidth())
        self.checkBox_applyFilters.setSizePolicy(sizePolicy)
        self.checkBox_applyFilters.setStyleSheet("font: 10pt \"System-ui\";")
        self.checkBox_applyFilters.setObjectName("checkBox_applyFilters")
        self.verticalLayout_4.addWidget(self.checkBox_applyFilters)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout.addWidget(self.horizontalWidget_2, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setStyleSheet("background-color: rgb(44, 47, 51);\n"
"font: 15pt \"System-ui\";\n"
"color: gray;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.flightsTable = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.flightsTable.setShowGrid(True)
        self.flightsTable.setObjectName("flightsTable")
        self.flightsTable.setColumnCount(7)
        self.flightsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.flightsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.flightsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.flightsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.flightsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.flightsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.flightsTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.flightsTable.setHorizontalHeaderItem(6, item)
        self.flightsTable.horizontalHeader().setVisible(True)
        self.flightsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.flightsTable.horizontalHeader().setDefaultSectionSize(111)
        self.flightsTable.horizontalHeader().setSortIndicatorShown(True)
        self.flightsTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_5.addWidget(self.flightsTable)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlightsAround"))
        self.pushButton_flightRadar.setText(_translate("MainWindow", "Go to FlightRadar"))
        self.pushButton_googleMaps.setText(_translate("MainWindow", "Go to GoogleMaps"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_configureFilters.setText(_translate("MainWindow", "Configure filters"))
        self.location_edit.setPlaceholderText(_translate("MainWindow", "Location"))
        self.radius_edit.setPlaceholderText(_translate("MainWindow", "Raius"))
        self.comboBox.setItemText(0, _translate("MainWindow", "km"))
        self.comboBox.setItemText(1, _translate("MainWindow", "mi"))
        self.pushButton_search.setText(_translate("MainWindow", "Search"))
        self.checkBox_applyFilters.setText(_translate("MainWindow", "Apply Filters"))
        self.label.setText(_translate("MainWindow", "No flights found in the area"))
        item = self.flightsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "callsign"))
        item = self.flightsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "line ICAO"))
        item = self.flightsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "model"))
        item = self.flightsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "departure"))
        item = self.flightsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "departure time"))
        item = self.flightsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "arrival"))
        item = self.flightsTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "arrival time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
