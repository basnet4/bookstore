import mysql.connector as mc


class DBConnect:
    def __init__(self):
        self.con = mc.connect(host='localhost', user='root', password='#Dr@cary$_4%', database='bookstore')
        self.cur = self.con.cursor()

    def insert(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()
        return self.cur.rowcount

    def select(self, query, values):
        self.cur.execute(query, values)
        info = self.cur.fetchall()
        return info

    def update(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()
        return self.cur.rowcount

    def delete(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def fetch(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchone()
        return rows

    # def __del__(self):
    #     if self.cur:
    #         self.cur.close()
    #     if self.con:
    #         self.con.close()
