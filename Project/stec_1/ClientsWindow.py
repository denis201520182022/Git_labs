from PyQt5.QtWidgets import QDialog
from ui.clients_ui import Ui_Dialog  # путь зависит от структуры проекта

class ClientsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Справочник клиентов")
