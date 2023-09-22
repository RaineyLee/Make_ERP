import sys
sys.path.append("C:\\Python Workplace\\Make_ERP\\db") #모듈 import가 안 될때 경로를 지정해 주기
import db_info as conn_info
import pymysql
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Insert:

    def __init__(self):
        db_info = conn_info.Connect()

        self.host = db_info.host
        self.user = db_info.username
        self.passwd = db_info.password
        self.db = db_info.database
        self.port = db_info.port

        self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, port=self.port, use_unicode=True, charset='utf8')        

    def insert_location(self, arr_1):
        cursor = self.conn.cursor()

        try:
            query = "TRUNCATE TABLE item_location;"
            cursor.execute(query)
            self.conn.commit()

            query = """INSERT INTO item_location (id, name, location, brand, package, c_date) VALUES (%s, %s, %s, %s, %s, now());"""
            cursor.executemany(query, arr_1)
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            error = ("Error", str(e))
            return error

        return ("완료", "제품위치 정보가 정상적으로 업로드 되었습니다.")

    def insert_barcode(self, arr_1):
        cursor = self.conn.cursor()

        try:
            query = "TRUNCATE TABLE item_barcode;"
            cursor.execute(query)
            self.conn.commit()

            query = """INSERT INTO item_barcode (id, alias, name, barcode, sc_code, c_date) VALUES (%s, %s, %s, %s, %s, now());"""
            cursor.executemany(query, arr_1)
            self.conn.commit()
            self.conn.close()            
                        
        except Exception as e:
            error = ("Error", str(e))
            return error

        return ("완료", "바코드 정보가 정상적으로 업로드 되었습니다.")