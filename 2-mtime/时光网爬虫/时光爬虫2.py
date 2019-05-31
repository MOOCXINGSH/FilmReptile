import requests
import re
from bs4 import BeautifulSoup
import Agent
import csv
import sys
import datetime

movText = ["movName",
           "movType",
           "movTime",
           "movDate",
           "movWriters",
           "movCountry",
           "movDc",
           "movScore",
           "movNum",
           "isMov",
           "movId"]

start = int(sys.argv[1])

def getProxies():
     return Agent.get_ip()
    
def openWeb(movId,proxies):
    url = "http://movie.mtime.com/"+str(movId)+"/"
    cookies = {'cookie':'bid=zltPvV3Cnlo; ll="108296"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1558147811%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fredir%3Dhttps%253A%252F%252Fwww.douban.com%252Fpeople%252F190201345%252F%22%5D; _pk_id.100001.8cb4=516f6bcc24b7d7e6.1558118530.2.1558148835.1558119419.; __utma=30149280.2009090745.1558118531.1558118531.1558147812.2; __utmc=30149280; __utmz=30149280.1558147812.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __gads=ID=66778657373b80dc:T=1558118592:S=ALNI_MZcVV5Pc_tPcOm9_cSV2Np8qUnNfw; push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=DFC3D426241A7816B731C8B64E0D09D44|c888d659f47f99b5aa94ee5000ba35f5; douban-profile-remind=1; _pk_ses.100001.8cb4=*; __utmb=30149280.6.10.1558147812; __utmv=30149280.19020; dbcl2="190201345:TWQ5yFEAfJQ"; ck=t9ER; __utmt=1'}
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; \Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
    r = requests.get(url, cookies=cookies, headers=headers, proxies=proxies)
    r.encoding = 'utf-8'
    #print("网页请求状态码：%s\n"%r.status_code)
    if r.status_code == 200:
        return BeautifulSoup(r.text,"lxml")
    else:
        return r.status_code
#爬导演
def getMovInfo(soup):
    try:
        return soup.find('div',class_="__r_c_").get_text()
    except:
        return None
#名字
def getMovName(soup):
    try:
        return soup.find('div',class_="clearfix").get_text()
    except:
        return None
#时长剧情
def getMovInfo2(soup):
    try:
        return soup.find('div',class_="otherbox __r_c_").get_text()
    except:
        return None

#def getMovText(movInfo,key):
#    try:    
#        return str(re.compile(key +".*").findall(str(movInfo))[0])[len(key)+2:]
#    except:
#        return None


#影评
def getMovScore(soup):
    try:
        return soup.find('div',class_="grade_tool").get_text
    except:
        return None
def getMovNumber(soup):
    try:
        return soup.find('div',class_="rating_sum").span.string
    except:
        return None

#def isMov(soup):
#    try:
#        return soup.find('div',id="recommendations").i.string[4:6]
#    except:
#        return None

def write_csv(data_row):
    path  = "./data/"+str(start)+".csv"
    with open(path,'a+',encoding="utf-8") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data_row)

def saveMovText(movId,proxies):
    soup = openWeb(movId,proxies)
    if soup == 404:
        print("ID:%d没找到对应电影"%movId)
        #print("--------------------------------------------------------------------------------")
    else:
        movInfo = getMovInfo(soup)
        movText[10] = isMov(soup)
        #print(movText[10])
        if movText[10] == "电影":
            movText[0] = getMovName(soup)
            movText[1] = getMovText(movInfo,"导演")
            #movText[2] = getMovText(movInfo,"主演")
            #movText[3] = getMovText(movInfo,"编剧")
            #movText[4] = getMovText(movInfo,"类型")
            movText[5] = getMovText(movInfo,"制片国家/地区")
            movText[6] = getMovText(movInfo,"发行公司")
            movText[7] = getMovText(movInfo,"片长")
            movText[8] = getMovScore(soup)
            movText[9] = getMovNumber(soup)
            movText[11] = str(movId)
            write_csv(movText)
            print(movText)
            print("--------------------------------------------------------------------------------")


def run(start,end):
    ipList = Agent.get_ip()
    proxies = Agent.get_random_ip(ipList)
    for movId in range(start,end):
        try:
            saveMovText(movId,proxies)
        except:
            print("ID:%d 丢失代理"%movId)
            ipList = Agent.get_ip()
            proxies = Agent.get_random_ip(ipList)
            print(proxies)
            print("重新读取%s"%movId)
            saveMovText(movId,proxies)
            
            #print("--------------------------------------------------------------------------------")

'''
#text
ipList = Agent.get_ip()
proxies = Agent.get_random_ip(ipList)
soup = openWeb(2000000,proxies)
print(soup)
'''


'''
pip3 install bs4
pip3 install lxml

'''


startTime = datetime.datetime.now()


run(start*10000,start*10000+100000)

endTime = datetime.datetime.now()
print(startTime)
print(endTime)


