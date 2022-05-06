from .info import _database
import pymysql


class Utils:
    def __init__(self):
        self._info = _database

    def conn(self, db_name):
        try:
            conn = pymysql.connect(host=self._info.db_info[db_name]['host'],
                                   port=self._info.db_info[db_name]['port'],
                                   user=self._info.db_info[db_name]['user'],
                                   passwd=self._info.db_info[db_name]['passwd'],
                                   db=db_name)
            print('connected')
            return conn
        except Exception as e:
            print('err')
            print(e)

    def insert_db(self, input_rows, input_conn, table_info):
        _conn = input_conn
        _curs = _conn.cursor()
        table_name = table_info['table_info']
        table_scheme = table_info['scheme']
        scheme_format = tuple(table_scheme)
        values_format = ['%s' for i in range(len(table_scheme))]
        values_format = tuple(values_format)

        try:
            for row in input_rows:
                sql = "INSERT INTO RAW.{}".format(table_name) + \
                    "({})".format(",\n ".join(scheme_format)) + \
                    " VALUES({})".format(",\n".join(values_format))
                _curs.excute(sql, row)
            _conn.commit()
            _conn.close()

        except Exception as e:
            print(e)
            _conn.commit()
            _conn.close()
