
# -*-encoding:utf-8-*-
import pytesseract
from PIL import Image
import cv2
import numpy as np
import os
import glob

def cv_imread(file_path):
    cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img

def ocrfile(filename):
    print("open ocrfile",filename)
    img = cv_imread(filename)
    if img is None:
        print("file is not img,pass:",filename)
        return
    cv2.imshow("OpenCV",img)
    cv2.waitKey(100)
    image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    #image.show()
    string = pytesseract.image_to_string(image,lang='chi_sim')
    print("Wadata2 BEGIN",string)
    print("Wadata2 END")

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
            print("to be ocr:",path)
            ocrfile(path)

