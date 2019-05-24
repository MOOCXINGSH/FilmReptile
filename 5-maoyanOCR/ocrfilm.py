# -*-encoding:utf-8-*-
import pytesseract
from PIL import Image
import cv2
import numpy as np
import os
import glob
import re

subtable=[
    ["战混","战狼2"],
    ["红诲","红海"],
    ["陲","睡"],
    ["祉潴","小猪"],
    ["孑L","孔"],
    ["恃工","特工"],
    ["拟眦","挑战"],
    ["ä良","狼"],
    ["羊m","羊"],
    ["-","."],
    ["ã良","狼"],
    ["昊","吴"],
    ["不皇","不是"]
]

def resuball(filmname):
    global subtable
    for subname in subtable:
        filmname=re.sub(subname[0],subname[1],filmname)
    return filmname

def cv_imread(file_path):
    #print("cv_imreawd",file_path)
    cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img

#猫眼截图
def ocrFile(filename):
    boxoffdict={}
    #print("open maoyan ocrfile",filename)
    img = cv_imread(filename)
    if img is None:
        print("file is not img,pass:",filename)
        return
    #片名
    x1,y1=270,230
    x2,y2=1100,410
    imgfocus=img[y1:y2,x1:x2]
    cv2.imshow("filmname",imgfocus)
    cv2.waitKey(50)
    image = Image.fromarray(cv2.cvtColor(imgfocus,cv2.COLOR_BGR2RGB))
    #image.show()
    filmnstr = pytesseract.image_to_string(image,lang='chi_sim')
    filmname=(filmnstr.split("\n"))[0]
    filmname=resuball(filmname)
    boxoffdict["影片名"]=filmname
    #上映时间地点
    x1,y1=290,520
    x2,y2=562,570
    imgfocus=img[y1:y2,x1:x2]
    cv2.imshow("filmtime",imgfocus)
    cv2.waitKey(1)
    image = Image.fromarray(cv2.cvtColor(imgfocus,cv2.COLOR_BGR2RGB))
    timeandplace = pytesseract.image_to_string(image)
    timeandplace=re.sub("o","0",timeandplace)
    timeandplace=re.sub("O","0",timeandplace)
    timeandplace=re.sub(" ","",timeandplace)
    mydatestrs=re.search("(\d+)-(\d+)-(\d{2})",timeandplace)
    g=mydatestrs.groups()
    timeandplace=g[0]+"-"+g[1]+"-"+g[2]
    boxoffdict["上映日期"]=timeandplace
    #print("\n 演出时间:",timeandplace)
    #类型
    x1,y1=290,410
    x2,y2=800,565
    imgfocus=img[y1:y2,x1:x2]
    cv2.imshow("filmtype",imgfocus)
    cv2.waitKey(50)
    image = Image.fromarray(cv2.cvtColor(imgfocus,cv2.COLOR_BGR2RGB))
    #image.show()
    filmtype = pytesseract.image_to_string(image,lang='chi_sim')
    filmtype=re.sub("云力","动",filmtype)
    filmtype=re.sub("斛幻","科幻",filmtype)
    filmtype=re.sub("晨情","爱情",filmtype)
    filmtype=re.sub("纪录片","纪实",filmtype)
    filmtype=re.sub("居比","剧",filmtype)
    filmtype=re.sub("惊喋","惊悚",filmtype)
    filmtype=re.sub(" ","",filmtype)
    filmtype=re.sub("3D","",filmtype)
    filmtype=re.sub("\|","",filmtype)
    filmtype=re.sub(",","",filmtype)    
    filmtype=re.sub("MAX","",filmtype)
    filmtype=re.sub("2D","",filmtype)
    filmtype=re.split("([\u4e00-\u9fa5]{2})",filmtype)
    filmtype="/".join(filmtype)
    filmtype=re.sub("//","/",filmtype)
    filmtype=filmtype[1:-1]
    filmtype=filmtype.split("/\n")[0]
    boxoffdict["类型"]=filmtype
    #print("\n 类型:",filmtype)
    #内地票房
    x1,y1=50,900
    x2,y2=750,1350
    imgfocus=img[y1:y2,x1:x2]
    cv2.imshow("boxoffice",imgfocus)
    cv2.waitKey(50)
    image = Image.fromarray(cv2.cvtColor(imgfocus,cv2.COLOR_BGR2RGB))
    #image.show()
    boxoffice = pytesseract.image_to_string(image,lang='chi_sim')
    boxoffice = re.sub(" ","",boxoffice)
    boxoffs=boxoffice.split("\n")
    #累计票房
    boxoffdict["累计票房"]=boxoffs[3]
    #首日票房
    boxoffdict["首日票房"]=boxoffs[9]
    #周首日票房
    boxoffdict["周首日票房"]=boxoffs[15]
    # 营销数据
    x1,y1=50,1390
    x2,y2=200,1450
    imgfocus=img[y1:y2,x1:x2]
    cv2.imshow("marketingdata",imgfocus)
    cv2.waitKey(50)
    image = Image.fromarray(cv2.cvtColor(imgfocus,cv2.COLOR_BGR2RGB))
    #image.show()
    marketingdata = pytesseract.image_to_string(image,lang='chi_sim')
    # 如果营销数据的位置上是北美票房，则试另一块区域
    if "北美票房" in marketingdata:
        x1,y1=50,1640
        x2,y2=200,1700
        imgfocus=img[y1:y2,x1:x2]
        cv2.imshow("marketingdata",imgfocus)
        cv2.waitKey(50)
        image = Image.fromarray(cv2.cvtColor(imgfocus,cv2.COLOR_BGR2RGB))
        #image.show()
        marketingdata = pytesseract.image_to_string(image,lang='chi_sim')
    
    if "营销数据" in marketingdata:
        x1,y1=x1,y1+100
        x2,y2=x2+800,y2+140
        imgfocus=img[y1:y2,x1:x2]
        cv2.imshow("marketingdata",imgfocus)
        cv2.waitKey(50)
        image = Image.fromarray(cv2.cvtColor(imgfocus,cv2.COLOR_BGR2RGB))
        #image.show()
        marketingdata = pytesseract.image_to_string(image,lang='chi_sim')
    else:
        marketingdata="物料总播放 微博指数 微信指数 百度指数 \n无 无 无 无"
    #去除数字中的空格    
    marketingdata="".join(re.split("(\d) ",marketingdata))
    #print("\n 营销数据:",marketingdata)
    marketingdata=re.sub("晌话题数","微博话题数",marketingdata)
    marketingdata=re.sub("舶话题数","微博话题数",marketingdata)
    mktdtitles=(marketingdata.split("\n"))[0].split(" ")
    mktdtconts=(marketingdata.split("\n"))[1].split(" ")
    for i in range(4):
        boxoffdict[mktdtitles[i]]=mktdtconts[i]
    print(boxoffdict)



#导演演员编剧完整图
def ocrFilmDirActInfo(filename):
    actordict={}
    print("open dir act compiler whole ocrfile",filename)
    img = cv_imread(filename)
    if img is None:
        print("file is not img,pass:",filename)
        return
    #电影名称
    x1,y1=130,110
    x2,y2=1100,180
    imgfocus=img[y1:y2,x1:x2]
    template = cv2.imread('./5-maoyanOCR/staffs.jpg')
    (h, w )= template.shape[:2]
    res = cv2.matchTemplate(imgfocus,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        #cv2.rectangle(imgfocus, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
        pass
    #cv2.imshow("imfocus1",imgfocus)
    #cv2.waitKey(10)
    #从员-开始
    imgfocus=imgfocus[0:y2-y1,pt[0]+w-90:1100]
    cv2.imshow("imfocus2",imgfocus)
    cv2.waitKey(10)
    h,w,c=imgfocus.shape
    wl=w
    num=int(w/wl)

    filmname=""
    for i in range(num):
        imgfocus_c=imgfocus[0:h,wl*i:wl*i+wl]
        cv2.imshow("imfocus_c",imgfocus_c)
        cv2.waitKey(1)       
        image = Image.fromarray(cv2.cvtColor(imgfocus_c,cv2.COLOR_BGR2RGB))
        filmname_c = pytesseract.image_to_string(image,lang='chi_sim')
        print(filmname_c)
        if filmname_c != "":
            filmname+=filmname_c
    #去掉开头的、员-
    filmname=filmname[3:]
    filmname=resuball(filmname)
    #print("影片名",filmname)
    actordict["影片名"]=filmname
    #类别
    x1,y1=40,200
    x2,y2=200,300
    imgfocus=img[y1:y2,x1:x2]
    cv2.imshow("filmtype",imgfocus)
    #cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),1)
    #cv2.imshow("OpenCV",img)
    cv2.waitKey(50)
    image = Image.fromarray(cv2.cvtColor(imgfocus,cv2.COLOR_BGR2RGB))
    #image.show()
    acttype = pytesseract.image_to_string(image,lang='chi_sim')
    acttype=acttype[0:2]
    print("类别：",acttype)
    #姓名
    y0=300
    H=330
    print("h",H)
    LH=H-50
    num=6
    namestr=""
    for i in range(num):
        x1,y1=250,y0+H*i
        x2,y2=900,y0+H*i+LH
        imgfocus=img[y1:y2,x1:x2]
        cv2.imshow("name",imgfocus)
        cv2.waitKey(1)
        image = Image.fromarray(cv2.cvtColor(imgfocus,cv2.COLOR_BGR2RGB)
        #image.show()
        name = pytesseract.image_to_string(image,lang='chi_sim')
        name = name.split("\n")
        name = re.sub(" ","",name[0])
        name = resuball(name)
        if name != "":
            namestr += name+"/"
    actordict[acttype]=namestr[0:-1]
    print(actordict)
    
#导演主演截图
def ocrFilmDirInfo(filename):
    #print("open file dir main act ocrfile",filename)
    img = cv_imread(filename)
    if img is None:
        print("file is not img,pass:",filename)
        return
    y0=393
    H=292
    print("h",H)
    LH=45
    num=7
    if "150443" not in filename:
        y0=y0+19
        H=H+1
    for i in range(num):
        x1,y1=200,y0+H*i
        x2,y2=800,y0+H*i+LH
        imgfocus=img[y1:y2,x1:x2]
        cv2.imshow("imfocus "+str(i),imgfocus)
        cv2.waitKey(1)
        image = Image.fromarray(cv2.cvtColor(imgfocus,cv2.COLOR_BGR2RGB))
        #image.show()
        mainactor = pytesseract.image_to_string(image,lang='chi_sim')
        print("Main acter",mainactor)
    

def walkandocr():
    path = "./"+os.sep
    for root,dirs,files in os.walk(path):
        for file in files:
            if root ==path:
                print(root+file)
            else:
                filename=root+os.sep+file
        for dirName in dirs:
            jpgfilename=root+os.sep+dirName+os.sep+"*.jpg"
            print(jpgfilename)
            paths=glob.glob(jpgfilename)
            print("paths",paths)
            paths.sort()
            for path in paths:
                print("\n Ocr:",path)
                if "导演演员编剧完整图" in path:
                    ocrFilmDirActInfo(path)
                    pass
                elif "导演主演截图" in path:
                    #ocrFilmDirInfo(path)
                    pass
                elif "猫眼" in path:
                    #ocrFile(path)
                    pass

#ocrFilmDirActInfo(".\\5-maoyanOCR\\导演演员编剧完整图\\Screenshot_20190522_120123_com.sankuai.moviepro.jpg")
walkandocr()
cv2.destroyAllWindows()
