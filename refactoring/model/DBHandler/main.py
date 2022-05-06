from .utils import Utils


class DBHandler:
    def __init__(self):
        self.utils = Utils()

    def conn(self, db_name):
        return self.utils.conn(db_name=db_name)

    def insert_db(self, conn, rows, table_info) -> None:
        self.utils.insert_db(input_rows=rows, input_conn=conn, table_info=table_info)
