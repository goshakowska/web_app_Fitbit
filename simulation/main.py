from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from ui_simulation_window import Ui_MainWindow
import sys
import backend_connection as bc

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.gym = None
        self.client = None
        self.trainer = None
        self.exercise = None
        self.param = None

        self._clients_list()
        self._gyms_list()
        self._exercises_list()

        self.ui.pushButton.clicked.connect(self._send_to_database)
        self.ui.gymList.itemClicked.connect(self._choose_gym)
        self.ui.clientList.itemClicked.connect(self._choose_client)
        self.ui.exerciseList.itemClicked.connect(self._choose_exercise)
        self.ui.trainerList.itemClicked.connect(self._choose_trainer)

    def _send_to_database(self):
        pass

    def _clients_list(self):
        self.ui.clientList.clear()
        clients = bc.get_clients()
        clients = sorted(clients, key=lambda client: client[0])
        for client in clients:
            description = f'{client[0]}.\t {client[1]}\t {client[2]}'
            item = QListWidgetItem(description)
            item.id = client[0]
            self.ui.clientList.addItem(item)

    def _gyms_list(self):
        self.ui.gymList.clear()
        gyms = bc.get_gyms()
        gyms = sorted(gyms, key=lambda gym: gym[0])
        for gym in gyms:
            description = f'{gym[0]}.\t{gym[1]}'
            item = QListWidgetItem(description)
            item.id = gym[0]
            self.ui.gymList.addItem(item)

    def _exercises_list(self):
        self.ui.exerciseList.clear()
        exercises = bc.get_exercises()
        exercises = sorted(exercises, key=lambda exercise: exercise['id'])
        for exercise in exercises:
            id = exercise['id']
            name = exercise['name']
            parameters = ''
            for id, par_name in exercise.get('parameters', []):
                parameters += par_name + ', '
            parameters = '(' + parameters[0:-2] + ')' if parameters else ''
            description = f'{id}.\t{name}\t{parameters}'
            item = QListWidgetItem(description)
            item.id = id
            item.param = exercise.get('parameters', [])
            self.ui.exerciseList.addItem(item)

    def _choose_gym(self, item):
        self.gym = item.id
        self.ui.trainerList.clear()
        self.trainer = None
        trainers = bc.get_trainers(self.gym)
        trainers = sorted(trainers, key=lambda trainer: trainer[0])
        for trainer in trainers:
            description = f'{trainer[0]}.\t{trainer[1]}\t{trainer[2]}'
            item = QListWidgetItem(description)
            item.id = trainer[0]
            self.ui.trainerList.addItem(item)

    def _choose_client(self, item):
        self.client = item.id
        print(self.client)

    def _choose_exercise(self, item):
        self.exercise = item.id
        self.param = item.param
        print(self.exercise)
        print(self.param)

    def _choose_trainer(self, item):
        self.trainer = item.id
        print(self.trainer)




def guiMain(args):
    app = QApplication(args)
    window = MainScreen()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)

