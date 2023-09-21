import os
import sys
import warnings

from openpyxl import *
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
main_window= uic.loadUiType(resource_path("C:\\Python Workplace\\Make_ERP\\windows\\upload_barcode.ui"))[0] # Window 사용시 ui 주소

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QWidget, main_window) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("바코드 정보")
        self.slots()

        self.date_edit.setDate(QDate.currentDate())
        self.date = self.date_edit.date().toString("yyyyMMdd")

        self._list = []   

    def slots(self):
        self.date_edit.dateChanged.connect(self.set_date)
        self.btn_open.clicked.connect(self.file_open)
        self.btn_select.clicked.connect(self.make_data)
        self.btn_upload.clicked.connect(self.upload)
        self.btn_close.clicked.connect(self.window_close)

    def set_date(self):
        self.date = self.date_edit.date().toString("yyyyMMdd")

    def file_open(self):
        fname = QFileDialog.getOpenFileName(parent=self, caption='Open file', directory='C:\\Users\\mynote\\Downloads')

        if fname[0]:
            self.text_select_file.setText(fname[0])
        else:
            self.text_select_file.setText("")
            QMessageBox.about(self, 'Warning', '파일을 선택하지 않았습니다.')

    def make_data(self):
        self.tbl_info.setRowCount(0) # clear()는 행은 그대로 내용만 삭제, 행을 "0" 호출 한다.
        file_name = self.text_select_file.toPlainText()

        from utils.make_data import Barcode
        make_data = Barcode(file_name)

        self._list = make_data.excel_data()
                
        self.make_table(len(self._list)-1, self._list)

    def make_table(self, num, arr_1):
        self.tbl_info.setRowCount(num)
        col = self.tbl_info.columnCount()

        for i in range(num):
            for j in range(self.tbl_info.columnCount()): # 아니면 10개
                self.tbl_info.setItem(i, j, QTableWidgetItem(arr_1[i][j]))

        # 컨텐츠의 길이에 맞추어 컬럼의 길이를 자동으로 조절
        ################################################################
        table = self.tbl_info
        header = table.horizontalHeader()

        for i in range(col):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
        ################################################################

        # 테이블의 길이에 맞추어 컬럼 길이를 균등하게 확장
            # self.tbl_info.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    # 테이블 선택범위 삭제
    def deleteRows(self):
        indexes = []
        rows = []

        for idx in self.tbl_info.selectedItems():
            indexes.append(idx.row())

        for value in indexes:
            if value not in rows:
                rows.append(value)

        # 삭제시 오류 방지를 위해 아래서 부터 삭제(리버스 소팅)
        rows = sorted(rows, reverse=True)

        # 선택행 삭제
        for rowid in rows:
            self.tbl_info.removeRow(rowid)

    def upload(self):
        from db.db_insert import Insert
        data_insert = Insert()
        result = data_insert.insert_barcode(self._list)

        self.msg_box(result[0], result[1])

    def progress_bar(self, arg):
        self.pbar = QProgressBar(self)
        self.pbar.setValue(arg)

    def msg_box(self, arg_1, arg_2):
        msg = QMessageBox()
        msg.setWindowTitle(arg_1)               # 제목설정
        msg.setText(arg_2)                          # 내용설정
        msg.exec_()                                 # 메세지박스 실행

    def window_close(self):
        self.close()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

# git 대소문자 구별하는 설정
# git config core.ignorecase false(true)