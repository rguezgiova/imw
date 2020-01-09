import pymysql.cursors

class DB():
    def __init__(self, username, password, database):
        self.connection = pymysql.connect(
            host='localhost',
            port=3306,
            user="ememt",
            password="Tenerife1998.",
            db="vmweb",
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def run(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            if sql.startswith('select'):
                return cursor.fetchall()
