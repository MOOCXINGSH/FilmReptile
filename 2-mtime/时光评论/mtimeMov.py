import requests
import re
from bs4 import BeautifulSoup
import csv
import sys
import datetime
import sys
from rwCsv import *
#处理 UNicodeENCODEERROR
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

movText = ["MovName",
           "UserScore",
           "UserCtime",
           "MovComment"]
         


def openWeb(movId):
    url = "http://movie.mtime.com/"+str(movId)+"/"
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; \Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
    r = requests.get(url,  headers=headers)
    r.encoding = 'utf-8'
    #print("网页请求状态码：%s\n"%r.status_code)
    if r.status_code == 200:
        return BeautifulSoup(r.text,"lxml")
    else:
        return r.status_code




def getMovName(soup):
    try:    
        return soup.find('div',class_="db_head").h1.string
    except:
        return None

def getMovType(soup):
    try:
        #print(getMovType(soup).find_all("a")[2])
         #movt=getMovType(soup).split("-")
         #print(movt[0])
        return soup.find('div',class_="otherbox __r_c_").get_text()
    except:
        return None




def getProxies():
     return Agent.get_ip()

def getUserLink(soup,num):
    try:  
        return soup.find_all('div',class_="pic_58")[num].a["href"]
    except :
        return None

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
        
        #print(getUserScore(soup)[13].span.string)
        for num in range(len(getUserName(soup))):
            act=[]
            try:
                act.append(getUserName(soup)[num].a["title"])
                act.append(getUserScore(soup,num))
                act.append(getUserCtime(soup)[num].a["entertime"])
                #act.append(getMovComment(soup,num).translate(non_bmp_map))
                act.append(getMovComment(soup,num)[num].h3.string)
                writeData(movName(movId)+".csv",act)
                print(act)
            except UnicodeEncodeError:
                act.append(getMovComment(soup,num)[num].h3.string.translate(non_bmp_map))
            except AttributeError:
                act.append("")
                
                
        




movId=readData("时光.csv")
def run():
    for i in range(77,81):
        soup = openIndexWeb(movId[i])
        
    
run()



