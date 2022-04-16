import logging.handlers
import os


class CustomLogger:
    def __init__(self):
        self.DirCheck()
        self.LoggerConfig = self.Config()


    def DirCheck(self):
        if not os.path.exists('./log'):
            os.mkdir('./log')


    def Config(self, log_name='LOG', log_dir='./log/log.out'):
        logger = logging.getLogger(log_name)
        fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s FunName:%(funcName)s > %(message)s')
        fileHandler = logging.FileHandler(log_dir)
        streamHandler = logging.StreamHandler()
        fileHandler.setFormatter(fomatter)
        streamHandler.setFormatter(fomatter)
        logger.addHandler(fileHandler)
        logger.addHandler(streamHandler)
        logger.setLevel(logging.DEBUG)
        return logger


    def Log(self, contents):
        self.LoggerConfig.info(contents)
