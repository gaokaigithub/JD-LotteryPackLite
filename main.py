#encoding=utf-8
import requests
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import csv
import datetime
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.setdefaultencoding('utf-8',) 
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
def loadCSVfile(file):
    csv_reader = csv.reader(open(file))
    return csv_reader
def lottery_time(userid,hour,minute,second):
    
    rows=loadCSVfile('cookies.csv')
    for each in rows:
        data.append(each)
print datetime.datetime.now().second 



'''
2.计算两个时间相差的秒数
>>> import datetime
>>> starttime = datetime.datetime.now()
>>> #long running
>>> endtime = datetime.datetime.now()
>>> print (endtime - starttime).seconds
3.计算当前时间向后10小时的时间
>>> d1 = datetime.datetime.now()
>>> d3 = d1 + datetime.timedelta(hours=10)
>>> d3.ctime()
'''
