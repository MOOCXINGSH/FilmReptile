import requests
import re
from bs4 import BeautifulSoup
import csv
import sys
import datetime
import sys
from rwCsv import *
from MovieName import *
#处理 UNicodeENCODEERROR
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

movText = ["UserName",
           "UserScore",
           "UserCtime",
           "MovComment"]
         

def getUserName(soup):
    try:
        return soup.find('h3',class_="fl hei px24")
    except:
        return None



def openIndexWeb():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    
    
    cookies={'cookie':'__utma=225482886.1981988927.1558785804.1558785804.1558785804.1;__utmb=225482886.12.10.1558785804;__utmc=225482886;__utmz=225482886.1558785804.1.1.utmcsr=movie.mtime.com|utmccn=(referral)|utmcmd=referral|utmcct=/208284/reviews/short/new.html;_utmx_=cdxI2fg9yCNAF2ljGxFa6uDL5OvDynrhvSPhvINpgiU='}

    url = "http://my.mtime.com/6109269/profile/"
    r = requests.get(url,cookies=cookies, headers=headers)
    r.encoding = 'utf-8'
    #print("网页请求状态码：%s\n"%r.status_code)
    soup = BeautifulSoup(r.text,"lxml")
    if r.status_code == 200:
        return BeautifulSoup(r.text,"lxml")
    else:
        return r.status_code
print(openIndexWeb())
#print(getUserName(soup))
    
       




