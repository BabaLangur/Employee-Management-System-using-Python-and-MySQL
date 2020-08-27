import mysql.connector
class connection():
    def __init__(self):
        self.conn =mysql.connector.connect(host='localhost',
                                                 database='epm',
                                                 user='root',
                                                 password='')
        self.my_cursor = self.conn.cursor()

    def iud(self,qry,values):
        try:
            self.my_cursor.execute(qry, values)
            self.conn.commit()
            return 1
        except Exception:
            return 0

    def show(self,qry):
        self.my_cursor.execute(qry)
        return self.my_cursor.fetchall()

    def search(self,qry):
        self.my_cursor.execute(qry)
        return self.my_cursor.fetchall()

    def pay(self,qry,values):
        self.my_cursor.execute(qry,values)
        self.conn.commit()
        return 1

