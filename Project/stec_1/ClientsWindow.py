import os
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from ui.clients_ui import Ui_Dialog

class ClientsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Справочник клиентов")

        # Абсолютный путь к базе относительно этого файла
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "db", "database.db")

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(db_path)
        if not self.db.open():
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть базу данных по пути:\n{db_path}")
            return

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable("clients")
        self.model.select()

        self.ui.table_clients.setModel(self.model)
        self.ui.table_clients.resizeColumnsToContents()

        self.ui.btn_add.clicked.connect(self.add_client)
        self.ui.btn_edit.clicked.connect(self.edit_client)
        self.ui.btn_delit.clicked.connect(self.delete_client)

    def add_client(self):
        QMessageBox.information(self, "Добавить", "Здесь будет добавление клиента")

    def edit_client(self):
        QMessageBox.information(self, "Редактировать", "Здесь будет редактирование клиента")

    def delete_client(self):
        QMessageBox.information(self, "Удалить", "Здесь будет удаление клиента")
