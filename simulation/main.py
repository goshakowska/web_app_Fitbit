from PySide2.QtWidgets import QApplication, QMainWindow
from ui_simulation_window import Ui_MainWindow
import sys
import requests

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # CONNECTION
        api_url = "http://localhost:8000/simulation/test_connection/"
        headers = {"Content-Type": "application/json"}

        body = {"message": "We are connected"}

        try:
            response = requests.post(api_url, json=body, headers=headers)

            if response.status_code == 200:
                print("Success")
            else:
                print(f"Error response {response.status_code}  {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")


def guiMain(args):
    app = QApplication(args)
    window = MainScreen()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)

