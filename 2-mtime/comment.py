import requests
import re
from bs4 import BeautifulSoup
import csv
import sys
import datetime
import sys

#处理 UNicodeENCODEERROR
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

movText = ["UserName",
           "UserScore",
           "UserCtime",
           "MovComment",
           "movType",
           "movCtry",
           "movDate",
           "movTime",
           "movScore",
           "movNum",
           "isMov",
           "movId"]
         
#用户名
def getUserName(soup):
    try:    
        return soup.find_all('div',class_="pic_58")
    except :
        return None


def getUserScore(soup,num):
     
     try:
          return soup.find_all("div",class_="pic_58")[num].span.string
     except AttributeError:
          return ""
def getUserCtime(soup):
     try:
          #a["entertime"]
          return soup.find_all("div",class_="mt10")
     except :
          return None

#电影评论
def getMovComment(soup,num):
    try:
        #print(getMovType(soup).find_all("a")[2])
        return soup.find_all('div',class_="mod_short")[num].h3.string
    except UnicodeEncodeError:
        return ""
def getProxies():
     return Agent.get_ip()

def getUserLink(soup,num):
    try:
        for link in soup.find_all('div',class_="pic_58")[num].a["href"]:
            
            
        return 
    except :
        return None

def write_csv(data_row):
    path  = "霸王.csv"
    with open(path,'a+',encoding="utf-8") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data_row)



def openIndexWeb(movId):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    for i in range(10):
        if i == 0:
            url = "http://movie.mtime.com/"+str(movId)+"/reviews/short/new.html"
        else:
            url= "http://movie.mtime.com/"+str(movId)+"/reviews/short/new-{}.html".format(str(i+1))
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        #print("网页请求状态码：%s\n"%r.status_code)
        soup = BeautifulSoup(r.text,"lxml")
        #print(len(getUserName(soup)))
        act=[]
        #print(getUserScore(soup)[13].span.string)
        for num in range(len(getUserName(soup))):
            act.append(getUserName(soup)[num].a["title"])
            act.append(getUserScore(soup,num))
            act.append(getUserCtime(soup)[num].a["entertime"])
            act.append(getMovComment(soup,num))
            
        print(act)





soup=openIndexWeb(10190)






def saveMovText(movId):
    soup = openWeb(movId,proxies)
    if soup == 404:
        print("ID:%d没找到对应电影"%movId)
        #print("--------------------------------------------------------------------------------")
    else:
         movt=getMovType(soup).split("-")
        #movInfo = getMovInfo(soup)
        #movText[10] = isMov(soup)
        #print(movText[10])
        #if movText[10] == "电影":
         movText[0] = getMovName(soup)
         movText[1] = getMovType(movt[1])
         movText[2] = getMovType(movt[0])
         movText[3] = getMovType(movt[2])
         movText[4] = timeP.getMovDoi(soup)
         movText[5] = timeP.getMovDoi(soup)
         movText[6] = timeP.getMovName(soup)
         movText[7] = timeC.getMovMc(soup)
         movText[8] = timeC.getMovDc(soup)
         #write_csv(movText)
         print(movText)
         print("--------------------------------------------------------------------------------")
'''


def saveMovText(movId):
    soup = openWeb(movId)
    if soup == 404:
        print("ID:%d没找到对应电影"%movId)
        #print("--------------------------------------------------------------------------------")
    else:
         movt=getMovType(soup).split("-")
         
        #movInfo = getMovInfo(soup)
        #movText[10] = isMov(soup)
        #print(movText[10])
        #if movText[10] == "电影":
         movText[0] = getMovName(soup)
         movText[2]= movt[1]
         movText[3] = movt[0]
         movText[4] = movt[2]
         movText[5] = timeP.act
         #movText[6] = timeP.getMovDoi(soup)
         #movText[6] = timeP.getMovName(soup)
         #movText[7] = timeC.getMovMc(soup)
         #movText[8] = timeC.getMovDc(soup)
         #write_csv(movText)
         #print(timeP.getMovDoi(soup))
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
