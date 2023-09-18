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
# main_window= uic.loadUiType(resource_path("/Users/black/projects/make_erp/main_window.ui"))[0] # Mac 사용시 ui 주소
main_window= uic.loadUiType(resource_path("C:\Python Workplace\Make_ERP\main_window.ui"))[0] # Window 사용시 ui 주소

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, main_window) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("구창_용인창고")
        # self.slots()

        outgoing = QAction('제품출고', self)
        outgoing.setStatusTip("제품출고")
        outgoing.triggered.connect(self.outgoing)

        menu_bar = self.menuBar()
        outgoing_menu = menu_bar.addMenu("출고")
        file_menu = menu_bar.addMenu("입고")
        file_menu = menu_bar.addMenu("재고")

        outgoing_menu.addAction(outgoing)

        status_bar = self.statusBar()
        self.setStatusBar(status_bar)

    def outgoing(self):
        print("new menu call")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()