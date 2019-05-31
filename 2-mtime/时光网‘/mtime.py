import requests
import re
from bs4 import BeautifulSoup
import csv
import sys
import datetime
import sys
#from rwCsv import *
#from MovieName import *
#处理 UNicodeENCODEERROR
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

movText = ["UserName",
           "UserScore",
           "UserCtime",
           "MovComment"]
         



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
        return soup.find_all('div',class_="mod_short")
        #return soup.find_all('div',class_="mod_short")[num].h3.string
    #except UnicodeEncodeError:
    #    return ""
    except :
    #except AttributeError:
        return ""
def getProxies():
     return Agent.get_ip()

def getUserLink(soup,num):
    try:  
        return soup.find_all('div',class_="pic_58")[num].a["href"]
    except :
        return None

def write_csv(data_row):
    path  = "霸王.csv"
    with open(path,'a+',encoding="utf-8") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data_row)



def openWeb(movId):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    
    url = "http://movie.mtime.com/"+str(movId)+"/"
    r = requests.get(url,  headers=headers)
    r.encoding = 'utf-8'
    #print("网页请求状态码：%s\n"%r.status_code)
    if r.status_code == 200:
        return BeautifulSoup(r.text,"lxml")
    else:
        return r.status_code
    #print(len(getUserName(soup)))
    '''
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
    '''
            
            


#电影名字
def getMovName(soup):
    try:    
        return soup.find('div',class_="clearfix").h1.string
    except:
        return None

#电影类型
def getMovType(soup):
    try:
        #print(getMovType(soup).find_all("a")[2])
        return soup.find('div',class_="otherbox __r_c_").get_text()
    except:
        return None



soup= openWeb(10190)
print(len(getMovType(soup)))
print(getMovType(soup))


'''
movId=readData("时光.csv")
def run():
    for i in range(77,81):
        soup = openIndexWeb(movId[i])
        
    
run()
'''

