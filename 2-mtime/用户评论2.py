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
    except:
        return None

def openIndexWeb(movId):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    url= "http://movie.mtime.com/10190/reviews/short/new-3.html"
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    #print("网页请求状态码：%s\n"%r.status_code)
    soup = BeautifulSoup(r.text,"lxml")
    #print(len(getUserName(soup)))
    act=[]
    #print(getUserScore(soup)[13].span.string)
    for num in range(len(getUserName(soup))):
        #act.append(getUserName(soup)[num].a["title"])
        #act.append(getUserScore(soup,num))
        #act.append(getUserCtime(soup)[num].a["entertime"])
        act.append(getMovComment(soup,num).translate(non_bmp_map))
    print(act)

soup=openIndexWeb(10190)
#print(getUserName(soup)[2].a["title"])
#print(getUserCtime(soup)[2].a["entertime"])
