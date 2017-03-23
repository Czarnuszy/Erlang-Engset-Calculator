from PyQt5.QtWidgets import QMessageBox, QWidget, QGroupBox, QVBoxLayout, QRadioButton, QGridLayout, QTabWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox
from PyQt5.QtCore import pyqtSlot


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # Add tabs
        self.tabs.addTab(self.tab1, "Erlang")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")


        # Create tab1 Labels and fields
        self.tab1.layout = QGridLayout(self)
        self.BlockRate = QLineEdit()
        self.Lines = QLineEdit()
        self.Traffic = QLineEdit()
        self.BlockRate.setDisabled(True)

        self.TrafficLabel = QLabel("Traffic:")
        self.BlockLabel = QLabel("Blocking Rate:")
        self.LinesLabel = QLabel("Lines:")

        # Create tab1 buttons
        self.LockTrafficBtn = QRadioButton("Lock Traffic")
        self.LockLinesBtn = QRadioButton("Lock Lines")
        self.LockBlockRateBtn = QRadioButton("Lock Blocking Rate")
        self.LockBlockRateBtn.setChecked(True)

        self.RadioGroup = QGroupBox()

        self.RadioGroup.layout = QVBoxLayout(self)
        self.RadioGroup.layout.addWidget(self.LockBlockRateBtn)
        self.RadioGroup.layout.addWidget(self.LockLinesBtn)
        self.RadioGroup.layout.addWidget(self.LockTrafficBtn)
        self.RadioGroup.setLayout(self.RadioGroup.layout)
        self.calculateBtn = QPushButton("Calculate")
        self.exitBtn = QPushButton("Exit")

        # Create tab1 layout
        self.tab1.layout.addWidget(self.TrafficLabel, 0, 0)
        self.tab1.layout.addWidget(self.Traffic, 0, 1)
        self.tab1.layout.addWidget(self.LinesLabel, 0, 2)
        self.tab1.layout.addWidget(self.Lines, 0, 3)
        self.tab1.layout.addWidget(self.BlockLabel, 0, 4)
        self.tab1.layout.addWidget(self.BlockRate, 0, 5)
        self.tab1.layout.addWidget(self.RadioGroup, 1, 5)
        self.tab1.layout.addWidget(self.calculateBtn, 2, 4)
        self.tab1.layout.addWidget(self.exitBtn, 2, 5)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


        #Button functions
        self.exitBtn.clicked.connect(self.exit_func)
        self.LockBlockRateBtn.clicked.connect(self.LockBlock)
        self.LockTrafficBtn.clicked.connect(self.LockTraffic)
        self.LockLinesBtn.clicked.connect(self.LockLines)
        self.calculateBtn.clicked.connect(self.Calculate)

    def Calculate(self):
        try:
            if not self.Traffic.isEnabled():
                var1 = int(self.Lines.text())
                var2 = float(self.BlockRate.text())

            elif not self.Lines.isEnabled():
                var1 = float(self.Traffic.text())
                var2 = float(self.BlockRate.text())
            elif not self.BlockRate.isEnabled():
                var1 = int(self.Lines.text())
                var2 = float(self.Traffic.text())
        except ValueError:
            QMessageBox.warning(self, "ERROR", "Wrong input data", QMessageBox.Ok)



    def LockBlock(self):
        self.Traffic.setEnabled(True)
        self.Lines.setEnabled(True)
        self.BlockRate.setEnabled(False)

    def LockLines(self):
        self.Traffic.setEnabled(True)
        self.Lines.setEnabled(False)
        self.BlockRate.setEnabled(True)

    def LockTraffic(self):
        self.Traffic.setEnabled(False)
        self.Lines.setEnabled(True)
        self.BlockRate.setEnabled(True)

    def exit_func(self):
        exit()

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

