import sys
sys.path.append("C:\\Python Workplace\\Make_ERP\\db") #모듈 import가 안 될때 경로를 지정해 주기
import db_info as conn_info
import pymysql
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Select:

    def __init__(self):
        db_info = conn_info.Connect()

        self.host = db_info.host
        self.user = db_info.username
        self.passwd = db_info.password
        self.db = db_info.database
        self.port = db_info.port

        self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, port=self.port, use_unicode=True, charset='utf8')        

    def select_location(self, arr_1):
        cursor = self.conn.cursor()

        try:            
            query = """SELECT A.id, A.name, A.location, A.brand, A.package, DATE_FORMAT(A.c_date, '%Y-%m-%d'), DATE_FORMAT(A.u_date, '%Y-%m-%d') FROM(SELECT id, name, location, brand, package, c_date, u_date FROM item_location WHERE u_date BETWEEN '2023-09-21' AND '2023-09-23') AS A;""" #날짜를 비교 하기 위해 안쪽 select문 사용, qt 테이블 입력을 위해 날짜 형식을 문자로 바꾸려고 밖의 select문 사용
            cursor.execute(query)
            result = cursor.fetchall()

            if result:                
                self.conn.close()
                self.msg_box("조회완료", "정상적으로 조회 되었습니다.")
                return result
            else:
                self.conn.close()
                self.msg_box("조회결과", "조회결과가 없습니다.")            

        except Exception as e:
            self.msg_box("Error", str(e))


    def msg_box(self, msg_1, msg_2):
        msg = QMessageBox()
        msg.setWindowTitle(msg_1)               # 제목설정
        msg.setText(msg_2)                          # 내용설정
        msg.exec_()                                 # 메세지박스 실행

    # def insert_barcode(self, arr_1):
    #     cursor = self.conn.cursor()

    #     try:
    #         query = "TRUNCATE TABLE item_barcode;"
    #         cursor.execute(query)
    #         self.conn.commit()

    #         query = """INSERT INTO item_barcode (id, alias, name, barcode, sc_code, c_date) VALUES (%s, %s, %s, %s, %s, now());"""
    #         cursor.executemany(query, arr_1)
    #         self.conn.commit()
    #         self.conn.close()            
                        
    #     except Exception as e:
    #         error = ("Error", str(e))
    #         return error

    #     return ("완료", "바코드 정보가 정상적으로 업로드 되었습니다.")