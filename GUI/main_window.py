import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from GUI import tabView


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table_widget = tabView.MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        # self.resize(800, 600)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())