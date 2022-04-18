from .utils.DBinfo import etc
from .utils.CustomLogger import CustomLogger
from .ErrHandler import ErrorHandler
import pymysql


class DBHandler:
    def __init__(self):
        self.DB_INFO = etc.DB_INFO


    def conn(self, DB_NAME):
        try:
            conn = pymysql.connect(host=self.DB_INFO[DB_NAME]['host'],
                                port=self.DB_INFO[DB_NAME]['port'],
                                user=self.DB_INFO[DB_NAME]['user'],
                                passwd=self.DB_INFO[DB_NAME]['passwd'],
                                db=self.DB_INFO[DB_NAME]['db'])
            CustomLogger().Log(f"{DB_NAME}: connection established!")
            return conn
        except Exception as conn_err:
            ErrorHandler().Err_check(err_list=None, err_name=type(conn_err).__name__)


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
            print(e)
            conn.commit()
            conn.close()
