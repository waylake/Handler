from inspect import isclass
import selenium.common.exceptions as selenium_exceptions
import urllib3.exceptions as urllib3_exceptions


def SeleniumErrList():
    """get the all errors from slenium and urllib3"""
    selenium_err = [x for x in dir(selenium_exceptions) if isclass(
        getattr(selenium_exceptions, x))]
    return selenium_err


def Urllib3ErrList():
    """get the all errors from slenium and urllib3"""
    urllib3_err = [x for x in dir(urllib3_exceptions) if isclass(
        getattr(urllib3_exceptions, x))]
    return urllib3_err

