from .utils.DBinfo import etc
import pymysql


class DBHandler:
    def __init__(self):
        self.CustomLogger = CustomLogger()
        self.DB_INFO = self.selectDB()


    def selectDB(self, DB_NAME=None):
        if DB_NAME in etc.DB_LIST:
            return etc.DB_INFO[DB_NAME]


    def conn(self):
        conn = pymysql.connect(host=self.DB_INFO['host'],
                               port=self.DB_INFO['port'],
                               user=self.DB_INFO['user'],
                               passwd=self.DB_INFO['passwd'],
                               db=self.DB_INFO['db'])
        return conn


    def insert_db(self, input_rows, table_info):
        table_name = table_info['table_name']
        table_scheme = table_info['scheme']
        scheme_format = tuple(table_scheme)
        values_format = ['%s' for i in range(len(table_scheme))]
        values_format = tuple(values_format)

        try:
            conn = self.conn()
            curs = conn.cursor()
            for row in input_rows:
                sql = "INSERT INTO RAW.{}".format(table_name) + \
                        "({})".format(",\n ".join(scheme_format)) + \
                        " VALUES({})".format(",\n".join(values_format))
                curs.execute(sql, row)
            conn.commit()
            conn.close()

        except Exception as e:
            self.CustomLogger.Log(contents=f'New errr Checked: {err_name}')
            print(e)
            conn.commit()
            conn.close()
