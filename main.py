from .models.DBHandler import DBHandler
from .models.ErrHandler import ErrHandler


class Handlers:
    def __init__(self, db_handler: DBHandler, err_handler: ErrHandler):
        self.db_handler = db_handler
        self.err_handler = err_handler
