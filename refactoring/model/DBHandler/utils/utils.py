from .info import _database
import pymysql
from tqdm import tqdm


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
        table_name = self._info.table_info['table_info']
        table_scheme = self._info.table_info['scheme']
        scheme_format = tuple(table_scheme)
        values_format = ['%s' for i in range(len(table_scheme))]
        values_format = tuple(values_format)

        try:
            for row in tqdm(input_rows):
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

    def max_length_check(self, rows):
        """
        get each element's max length from rows
        """
        elements = [str(1) for i in range(len(rows[0]))]
        row_lens = [None for i in range(len(elements))]

        for rows_idx, row in enumerate(rows):
            for row_idx, row_element in enumerate(row):
                row_element_len = len(str(row_element))
                element_row_len = len(elements[row_idx])
                if row_element_len > element_row_len:
                    row_lens[row_idx] = row_element_len

        return row_lens
