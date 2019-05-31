import requests
from bs4 import BeautifulSoup

def openWeb():
    #修改url
    url = "http://movie.mtime.com/10190/"
    r = requests.get(url)
    r.encoding = 'utf-8'
    if r.status_code == 200:
        return BeautifulSoup(r.text,"lxml")
    else:
        return r.status_code

movText = ["movName",
           "movType",
           "movTime"]

soup = openWeb()

def getMovText(movInfo,key):
    try:    
        return str(re.compile(key +".*").findall(str(getMovInfo))[0])[len(key)+2:]
    except:
        return None
def getMovInfo(soup):
    try:
        return soup.find_all('dd',class_="__r_c_")
    except:
        return None


#movData = soup.find_all('div',class_="mov_pic")

#for num in range(0,10):
#     #print(movData[num].a["href"])
#     com_id=re.match(".*/(\d+)",movData[num].a["href"])
#     print(com_id.group(1))
#     f=open("时光网id.csv",'a',newline='')
#     f.write(com_id.group(1)+'\n')
#     f.close()
movText[0] = getMovText(getMovInfo,"导演")



print(movText)
