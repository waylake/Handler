from ..utils.CustomLogger import CustomLogger
from ..utils.ErrParserInfo import info as ErrParserInfo
from ..utils.DBinfo import etc
from ..utils import ErrParser
from .utils.utils import Utils
from .utils import info

import pymysql
import inspect
import pickle
import gzip
import sys
import os


class ErrHandler:
    def __init__(self):
        self.utils = Utils(info=info)
        self.utils.check_dir()
        self.loadedData = self.loadData()
        self.new_err_list = []

    def Err_check(self, err_name: Exception):
        """check the error is in the error list"""
        CustomLogger().Log(contents=f'Error Checked: {err_name}')

    def Err_list(self):
        err_list = []
        for ERR in ErrParserInfo.ERR_LIST:
            for Err_func in ErrParserInfo.ERR_INFO[ERR]:
                func_name = ErrParserInfo.ERR_INFO[ERR]['func']
                temp = eval(f"ErrParser.{func_name}()")
                err_list.extend(temp)
        return err_list

