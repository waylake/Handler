from utils.CustomLogger import CustomLogger
from utils import ErrParser

import utils.ErrParserInfo.info as ErrParserInfo
import inspect
import pickle
import gzip
import sys
import os


class ErrorHandler:
    def __init__(self):
        self.DirCheck()
        self.loadedData = self.loadData()
        self.new_err_list = []
        self.CustomLogger = CustomLogger()


    def DirCheck(self):
        if not os.path.exists('./ErrorHandler'):
            os.mkdir('./ErrorHandler/Data')
            os.mkdir('./ErrorHandler/Data/EO')
            os.mkdir('./ErrorHandler/Data/err')


    def loadData(self):
        try:
            data = self.loadPickle()
            return data
        except:
            data = None
            return data


    def Err_check(self, err_list, err_name):
        """check the error is in the error list"""
        if err_name in err_list:
            return True
        else:
            # new err_list
            self.new_err_list.append(err_name)
            self.saveToPickle(data=self.new_err_list)
            self.CustomLogger.Log(contents=f'New errr Checked: {err_name}')
            return False


    def saveToPickle(self, data):
        self.CustomLogger.Log(contents='Save the new error list')
        # save and compress.
        with gzip.open('./ErrorHandler/Data/err/ERROR_LIST.pkl', 'wb') as f:
            pickle.dump(data, f)


    def loadPickle(self):
        self.CustomLogger.Log(contents='Loaded the saved err list')
        with gzip.open('./ErrorHandler/Data/err/ERROR_LIST.pkl', 'rb') as f:
            loaded = pickle.load(f)

        return loaded


    def Err_list(self):
        err_list = []
        for ERR in ErrParserInfo.ERR_LIST:
            for Err_func in ErrParserInfo.ERR_INFO[ERR]:
                func_name = ErrParserInfo.ERR_INFO[ERR]['func']
                err_list.extend(eval(f"ErrParser.{func_name}()"))

        return err_list

