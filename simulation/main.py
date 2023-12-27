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
        self.equipment = None
        self.exercise = None
        self.param = None
        self.equip_list = False


        self._clear()

        self.ui.pushButton.clicked.connect(self._send_to_database)
        self.ui.gymList.itemClicked.connect(self._choose_gym)
        self.ui.clientList.itemClicked.connect(self._choose_client)
        self.ui.exerciseList.itemClicked.connect(self._choose_exercise)
        self.ui.equipmentList.itemClicked.connect(self._choose_equipment)

    def _send_to_database(self):
        end_time = datetime.now()
        if not self.gym or not self.client or not self.exercise:
            dialog = Dialog('Najpierw wybierz ćwiczenie,\nklienta i siłownię', self)
            dialog.show()
        elif self.equip_list and not self.equipment:
            dialog = Dialog('Najpierw wybierz urządzenie', self)
            dialog.show()
        else:
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
            bc.insert_exercise_history(start_time, duration, repetitions_number, self.gym, self.exercise, self.equipment, self.client, calories, param)
            dialog = Dialog('Dodano ćwiczenie', self)
            dialog.show()
            self._clear()



    def _clear(self):
        # lists
        self._gyms_list()
        self._exercises_list()
        self.ui.clientList.clear()
        self.ui.equipmentList.clear()
        # list's items
        self.equip_list = False
        self.gym = None
        self.client = None
        self.exercise = None
        self.param = None
        self.equipment = None
        # spinboxes
        self.ui.time.setValue(0)
        self.ui.repetitionsNumber.setValue(0)
        self.ui.distance.setValue(0)
        self.ui.weight.setValue(0)
        self.ui.hight.setValue(0)
        self.ui.calories.setValue(0)


    def _clients_list(self):
        self.ui.clientList.clear()
        clients = bc.get_clients(self.gym)
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
            exercise_id = exercise['id']
            name = exercise['name']
            parameters = ''
            param_id = []
            for id, par_name in exercise.get('parameters', []):
                param_id.append(id)
                parameters += par_name + ', '
            parameters = '(' + parameters[0:-2] + ')' if parameters else ''
            description = f'{exercise_id}.\t{name}\t{parameters}'
            item = QListWidgetItem(description)
            item.id = exercise_id
            item.param = param_id
            self.ui.exerciseList.addItem(item)

    def _equipments_list(self):
        self.ui.equipmentList.clear()
        equipments = bc.get_equipments(self.gym, self.exercise)
        if equipments:
            self.equip_list = True
        equipments = sorted(equipments, key=lambda equipment: equipment[0])
        for equipment in equipments:
            description = f'{equipment[0]}.\t {equipment[1]}'
            item = QListWidgetItem(description)
            item.id = equipment[0]
            self.ui.equipmentList.addItem(item)

    def _choose_gym(self, item):
        self.client = None
        self.gym = item.id
        self._clients_list()
        if self.exercise is not None:
            self._equipments_list()

    def _choose_client(self, item):
        self.client = item.id

    def _choose_exercise(self, item):
        self.exercise = item.id
        self.param = item.param
        self.equip_list = False
        if self.gym is not None:
            self._equipments_list()

    def _choose_equipment(self, item):
        self.equipment = item.id



class Dialog(QDialog):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(text)
        self.ui.pushButton.clicked.connect(self.close)


def guiMain(args):
    app = QApplication(args)
    window = MainScreen()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)

