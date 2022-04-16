from handlers.DBHandler import DBHandler
from handlers.ErrHandler import ErrorHandler



DBHandler = DBHandler()
conn = DBHandler.conn('RAW')

