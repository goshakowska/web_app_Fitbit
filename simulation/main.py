from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QDialog
from ui_simulation_window import Ui_MainWindow
from ui_dialog import Ui_Dialog
import sys
import backend_connection as bc
from datetime import datetime, timedelta

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


        self._clear()

        self.ui.pushButton.clicked.connect(self._send_to_database)
        self.ui.gymList.itemClicked.connect(self._choose_gym)
        self.ui.clientList.itemClicked.connect(self._choose_client)
        self.ui.exerciseList.itemClicked.connect(self._choose_exercise)
        self.ui.trainerList.itemClicked.connect(self._choose_trainer)

    def _send_to_database(self):
        end_time = datetime.now()
        if not self.gym or not self.client or not self.exercise:
            dialog = Dialog(self)
            dialog.show()
        duration = self.ui.time.value()
        start_time = end_time  - timedelta(seconds=duration)
        start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
        repetitions_number = self.ui.repetitionsNumber.value()
        calories = self.ui.calories.value()
        param = {}
        if 1 in self.param:
            param[1] = self.ui.weight.value()
        if 2 in self.param:
            param[2] = self.ui.distance.value()
        if 3 in self.param:
            param[3] = self.ui.hight.value()
        bc.insert_exercise_history(start_time, duration, repetitions_number, self.gym, self.exercise, self.trainer, self.client, calories, param)

    def _clear(self):
        # lists
        self._clients_list()
        self._gyms_list()
        self._exercises_list()
        # list's items
        self.gym = None
        self.client = None
        self.trainer = None
        self.exercise = None
        self.param = None
        # spinboxes
        self.ui.time.setValue(0)
        self.ui.repetitionsNumber.setValue(0)
        self.ui.distance.setValue(0)
        self.ui.weight.setValue(0)
        self.ui.hight.setValue(0)
        self.ui.calories.setValue(0)


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
            param_id = []
            for id, par_name in exercise.get('parameters', []):
                param_id.append(id)
                parameters += par_name + ', '
            parameters = '(' + parameters[0:-2] + ')' if parameters else ''
            description = f'{id}.\t{name}\t{parameters}'
            item = QListWidgetItem(description)
            item.id = id
            item.param = param_id
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



class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)


def guiMain(args):
    app = QApplication(args)
    window = MainScreen()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)

