import mysql.connector as mc


class DBConnect:
    def __init__(self):
        self.con = mc.connect(host='localhost', user='root', password='#Dr@cary$_4%', database='bookstore')
        self.cur = self.con.cursor()

    def insert(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def select(self, query, values):
        self.cur.execute(query, values)
        info = self.cur.fetchall()
        return info