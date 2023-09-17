from openpyxl import *
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5 import uic

# 절대경로를 상대경로로 변경 하는 함수
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
main_window= uic.loadUiType(resource_path("/Users/black/projects/make_erp/main_window.ui"))[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, main_window) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("구창_용인창고")
        # self.slots()

        new_action = QAction('$New', self)
        new_action.setStatusTip("새파일생성")
        new_action.triggered.connect(self.menu_newcall)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(new_action)

        status_bar = self.statusBar()
        self.setStatusBar(status_bar)

    def menu_newcall(self):
        print("new menu call")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()