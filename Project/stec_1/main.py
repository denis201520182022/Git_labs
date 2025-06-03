import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main_window_ui import Ui_MainWindow
from ClientsWindow import ClientsWindow  # твой файл с окном клиентов

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.clients_window = None
        self.ui.actionClients.triggered.connect(self.open_clients_window)

    def open_clients_window(self):
        if self.clients_window is None:
            self.clients_window = ClientsWindow()
        self.clients_window.show()
        self.clients_window.raise_()
        self.clients_window.activateWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
