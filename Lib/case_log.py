import logging
import os
import sys

def log(func):
    def log_case_info(*args,**kwargs):
        #logger = logging.getLogger('func')
        res = func(*args,**kwargs)
        logging.info("func:{func._name_}")
        return res
    return log_case_info
