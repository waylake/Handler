from .models.DBHandler import DBHandler
from .models.ErrHandler import ErrorHandler


class Handlers:
    def __init__(self, db_handler: DBHandler,
                 err_handler: ErrorHandler):
        self.db_handler = db_handler
        self.err_handler = err_handler

