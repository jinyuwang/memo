# -*- coding:utf8 -*-

import time
from datetime import datetime

WEEK_TABLE = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]

def _islist(v):
    return isinstance(v, list) or isinstance(v, tuple)

def _isdict(v):
    return isinstance(v, dict)

def _isstr(s):
    return isinstance(s, basestring)

# *******************************************************
# reutn : 1469806246
def get_cur_timestamp():
    return int(time.time())

# return : '2016-07-29 23:30:35'
def get_cur_strtime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_cur_weekday():
	index = datetime.today().weekday() + 1
	return WEEK_TABLE[int(index)]

# return : '2016-07-29'
def get_cur_strdate():
    return datetime.now().strftime('%Y-%m-%d')