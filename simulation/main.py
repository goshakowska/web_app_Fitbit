from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from ui_simulation_window import Ui_MainWindow
import sys
import backend_connection as bc

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self._send_to_database)
        self._clients()
        self._gyms()

    def _send_to_database(self):
        pass

    def _clients(self):
        self.ui.clientList.clear()
        clients = bc.get_clients()
        clients = sorted(clients, key=lambda client: client[0])
        for client in clients:
            description = f'{client[0]}.\t {client[1]}\t {client[2]}'
            item = QListWidgetItem(description)
            item.id = client[0]
            self.ui.clientList.addItem(item)

    def _gyms(self):
        self.ui.gymList.clear()
        gyms = bc.get_gyms()
        gyms = sorted(gyms, key=lambda gym: gym[0])
        for gym in gyms:
            description = f'{gym[0]}.\t{gym[1]}'
            item = QListWidgetItem(description)
            item.id = gym[0]
            self.ui.gymList.addItem(item)

    def _exercises(self):
        pass





def guiMain(args):
    app = QApplication(args)
    window = MainScreen()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)

