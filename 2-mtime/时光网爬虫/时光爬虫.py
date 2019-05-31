import requests
from bs4 import BeautifulSoup
import re
import csv

#定义爬取函数
def get_infos(htmls, csvname):
    #信息头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    #flag在写入文件时判断是否为首行
    flag = True
    #判断第一页网址，第二页及其后的网址
    for i in range(10):
        if i == 0:
            html = htmls
        else:
            html = htmls + 'index-{}.html'.format(str(i+1))
        res = requests.get(html, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')
        alls = soup.select('#asyncRatingRegion > li') #选取网页的li节点的内容
        #对节点内容进行循环遍历
        for one in alls:
            #paiming = one.a.em.string     #排名
            p1 = one.find(name='span', attrs={'class': 'total'}, text=re.compile('\d'))     #评分在两个节点，
            p2 = one.find(name='span', attrs={'class': 'total2'}, text=re.compile('.\d'))
            
            #判断评分是否为空
            if p1 and p2 != None:
                p1 = p1.string
                p2 = p2.string
            else:
                p1 = 'no'
                p2 = ' point'
            point = p1 + p2 + '分'
            numbers = one.find(text=re.compile('评分'))   #评分数量
            print(point)
            '''
            # 保存为csv
            csvnames = 'C:\\' + csvname + '.csv'
            with open(csvnames, 'a+', encoding='utf-8') as f:
                writer = csv.writer(f)
                if flag:
                    writer.writerow(('paiming', 'name', 'realcontent', 'point', 'numbers'))
                writer.writerow((paiming, name, realcontent, point, numbers))
            flag = False
            '''

#调用函数
Japan_html = 'http://www.mtime.com/top/movie/top100_chinese/'
csvname1 = 'Japan_top'
get_infos(Japan_html, csvname1)
print(1)
