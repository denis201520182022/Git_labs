import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from ui.main_window_ui import Ui_MainWindow  # импортируем интерфейс
from ClientsWindow import ClientsWindow
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.clients_window = None

        # Подключаем обработчик нажатия на пункт меню
        self.ui.actionClients.triggered.connect(self.open_clients_window)

    def open_clients_window(self):
        try:
            print("Открываю окно клиентов")
            if self.clients_window is None:
                self.clients_window = ClientsWindow()
            self.clients_window.show()
        except Exception as e:
            print(f"Ошибка при открытии окна клиентов: {e}")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())


