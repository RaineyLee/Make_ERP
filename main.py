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

        menubar = self.menuBar()
        Filemenu = menubar.addMenu("파일")
        Filemenu1 = menubar.addMenu("편집")
        Filemenu2 = menubar.addMenu("서식") 
        loadfile = QAction('laod File ...', self) 
        savefile = QAction('save File ...', self) 
 
        # loadfile.triggered.connect(self.add_open) 
        # savefile.triggered.connect(self.add_save) 
        # exit.triggered.connect(qApp.quit) 
        # Filemenu.addAction(loadfile) 
        # Filemenu.addAction(savefile) 
        # Filemenu.addAction(exit)

        self.show()

        # self.date_edit.setDate(QDate.currentDate())
        # self.date = self.date_edit.date().toString("yyyyMMdd")

        

    # def slots(self):
    #     self.date_edit.dateChanged.connect(self.set_date)
    #     self.btn_close.clicked.connect(self.window_close)
    #     self.btn_file.clicked.connect(self.file_open)
    #     self.btn_activate.clicked.connect(self.excel_data)
    #     self.cmb_company.currentTextChanged.connect(self.change_index)

    # def change_index(self):
    #     if self.cmb_company.currentIndex() == int(0):
    #         self.line_SendNum.clear()
    #         self.line_OrderNum.clear()

    #     elif self.cmb_company.currentIndex() == int(1):
    #         self.line_SendNum.setText(str(2))
    #         self.line_OrderNum.setText(str(17))

    #     else:
    #         self.line_SendNum.setText(str(9))
    #         self.line_OrderNum.setText(str(28))


    # def file_open(self):
    #     fname = QFileDialog.getOpenFileName(parent=self, caption='Open file', directory='C:\\Guchang\\구창물류\\출고\\송장번호')

    #     if fname[0]:
    #         self.txt_file.setText(fname[0])
    #     else:
    #         QMessageBox.about(self, 'Warning', '파일을 선택하지 않았습니다.')

    # def window_close(self):
    #     self.close()

    # def set_date(self):
    #     self.date = self.date_edit.date().toString("yyyyMMdd")

    # def excel_data(self):
    #     wb = openpyxl.load_workbook(filename = self.txt_file.toPlainText())
    #     ws = wb.active
    #     # ws.insert_cols(2) #두번째 행(B행) 삽입
    #     # col = 'b'
    #     # count = 1
    #     deliver_num = []
        
    #     # 택배사 선택에 따따른  송장번호, 주문번호 변경 (경동택배, cj택배)
    #     for row in ws.iter_rows(min_row=2, values_only=True):
    #         num_w_text = self.cmb_company.currentText()[:1] + " " + self.line_SendNum.text() # 송장번호에 택배사 이름 추가
    #         order_num = self.line_OrderNum.text() # 출고지시 '주문번호'
    #         total_number = (order_num, num_w_text) # 위 두 번호를 튜블로 만듬
    #         deliver_num.append(total_number) # 최종 리스트에 추가

    #     wb.close()
    #     self.close()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()