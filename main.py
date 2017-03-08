#encoding=utf-8
import requests
import time
import re
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
def lottery_time(userid,code,timet,delay,cookielist,proxylist=[]):
    cookiedt=[]
    msglist=[]
    for each in cookielist:
        if str(each[0])==str(userid):
            cookiedt.append(each[1])
    proxies=[]
    if proxylist!=[]:
        ps=1 #代理模式开启
        for each in proxylist:
            address='http://'+str(each[0])+':'+str(each[1])
            proxies.append({'http':address})
   
    time1=datetime.datetime.strptime(timet,'%Y-%m-%d %H:%M:%S')
    enabled=1
    while enabled==1:
        
            
        if datetime.datetime.now()>=time1:
            for each in cookiedt:
                headers={'cookie':each,'Referer':'http://l.activity.jd.com/lottery/lottery_chance.action?lotteryCode='+code}
                if ps==1:
                    status=0
                    while status==0: 
                        try:
                            print proxies[0]
                            goprince=requests.get('http://l.activity.jd.com/lottery/lottery_start.action?lotteryCode='+code,headers=headers,proxies=proxies[0],verify=False).text
                            status=1
                        except:
                            print "Network Error!Change Proxy and Retrying……"
                            del proxies[0]
                if ps==0:
                    goprince=requests.get('http://l.activity.jd.com/lottery/lottery_start.action?lotteryCode='+code,headers=headers,verify=False).text
                winner=re.findall('"winner":(.*?)}',goprince,re.S)
                if str(winner)=='[u\'true\']':
                    print code
                    print goprince
                    msglist.append(goprince)
                ###########如需屏蔽未中奖消息，请注释如下内容
                else:
                    print code
                    print goprince
                    msglist.append(goprince)
                ###########----------------------------
                time.sleep(delay)
            enabled=0
            f=open('f.txt','a')
            for each in msglist:
                f.write(str(each))  
                f.write('\n')     
            f.close()
            print 'Finished!'
def add_lottery(userid,code,timet,delay,cookielist,proxylist=[]):
    threading.Thread(target=lottery_time,args=(userid,code,timet,delay,cookielist,proxylist)).start()
    print code
    time.sleep(0.1)
if __name__ == "__main__":            
    cookielist=loadCSVfile('cookies.csv') #加载Cookies文件
    #proxylist=loadCSVfile('ip.csv') #加载代理地址文件
    lottery_time('1','4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f','2017-03-08 20:57:30',5,cookielist,proxylist) #代理模式
    lottery_time('1','4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f','2017-03-08 20:57:30',5,cookielist) #无代理模式

