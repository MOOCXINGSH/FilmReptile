import requests
import re
from bs4 import BeautifulSoup



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


def getProxies():
     return Agent.get_ip()
    
def openWeb(movId):
    url = "http://movie.mtime.com/"+str(movId)+"/fullcredits.html"
    cookies = {'cookie':'bid=zltPvV3Cnlo; ll="108296"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1558147811%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fredir%3Dhttps%253A%252F%252Fwww.douban.com%252Fpeople%252F190201345%252F%22%5D; _pk_id.100001.8cb4=516f6bcc24b7d7e6.1558118530.2.1558148835.1558119419.; __utma=30149280.2009090745.1558118531.1558118531.1558147812.2; __utmc=30149280; __utmz=30149280.1558147812.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __gads=ID=66778657373b80dc:T=1558118592:S=ALNI_MZcVV5Pc_tPcOm9_cSV2Np8qUnNfw; push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=DFC3D426241A7816B731C8B64E0D09D44|c888d659f47f99b5aa94ee5000ba35f5; douban-profile-remind=1; _pk_ses.100001.8cb4=*; __utmb=30149280.6.10.1558147812; __utmv=30149280.19020; dbcl2="190201345:TWQ5yFEAfJQ"; ck=t9ER; __utmt=1'}
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; \Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
    r = requests.get(url, cookies=cookies, headers=headers)
    r.encoding = 'utf-8'
    #print("网页请求状态码：%s\n"%r.status_code)
    if r.status_code == 200:
        return BeautifulSoup(r.text,"xml")
    else:
        return r.status_code



soup = openWeb(10190)
'''

#演员
def getMovName(soup):
    try:
        return soup.find_all('div',class_="pic_58")
    except:
        return None
     


act=[]
for b in range(len(getMovName(soup))):
     act.append(getMovName(soup)[b].h3.string)
     #print(getMovName(soup)[b].h3.string)
print(act)

'''



def getMovDoi(soup):
    try:
        return soup.find('span',id="attitudeCountRegion")
    except:
        return None
act=[]
#for b in range(len(getMovDoi(soup))):
#     act.append(getMovDoi(soup).find_all("a")[b].string)
#print(getMovDoi(soup).find_all("a")[1].string)
print(getMovDoi(soup))

