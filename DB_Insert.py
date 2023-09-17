import pymysql
import DB_Info

class DB_Insert:

    def __init__(self):
        db_info = DB_Info.Connect()
        self.host = db_info.host
        self.user = db_info.username
        self.passwd = db_info.password
        self.db = db_info.database
        self.port = db_info.port

        self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, port=self.port, use_unicode=True, charset='utf8')
        self.cursor = self.conn.cursor()  

    def insert_location(self):
        query = "SELECT info FROM welcome"
        self.cursor.execute(query)
        self.conn.commit()

        rows = self.cursor.fetchone()
        self.cursor.close()
        self.conn.close()

        return rows