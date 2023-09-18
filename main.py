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
# main_window= uic.loadUiType(resource_path("/Users/black/projects/make_erp/main_window.ui"))[0] # Mac 사용시 ui 주소
main_window= uic.loadUiType(resource_path("C:\Python Workplace\Make_ERP\windows\main_window.ui"))[0] # Window 사용시 ui 주소

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

        inventory_location = QAction('제품위치', self)
        inventory_location.setStatusTip("제품위치")
        inventory_location.triggered.connect(self.inventory_location)

        menu_bar = self.menuBar()
        outgoing_menu = menu_bar.addMenu("출고")
        incommig_menu = menu_bar.addMenu("입고")
        inventory_menu = menu_bar.addMenu("재고")

        outgoing_menu.addAction(outgoing)
        inventory_menu.addAction(inventory_location)

        status_bar = self.statusBar()
        self.setStatusBar(status_bar)

    def outgoing(self):
        print("new menu call")

    def inventory_location(self):        
        import inventory_location as inv_loc

        self.location = inv_loc.WindowClass()
        self.location.show()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()