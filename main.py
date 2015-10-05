from __future__ import division
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib.pyplot import gray
from samba.dcerpc.dnsp import soa

global rakam
rakam=3
def nothing(x):
    global rakam
    rakam=x
    print "rakam===>",rakam
    pass

global rakam2
rakam2=3
def nothing2(x):
    global rakam2
    rakam2=x
    print "rakam2===>",rakam2
    pass



saban=cv2.imread('saban.jpg')


saban = cv2.cvtColor(saban,0)
saban = cv2.resize(saban, (640, 480))
cap = cv2.VideoCapture(1)

cv2.namedWindow('image')
cv2.createTrackbar('sayi1', 'image',1,255,nothing)
cv2.createTrackbar('sayi2', 'image',1,255,nothing2)




while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    img = cv2.cvtColor(frame,0)


    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    adaptive=imgray.copy()
    normal=imgray.copy()
    otsu=imgray.copy()
    imgray = cv2.GaussianBlur(imgray,(5,5),0)
    normal = cv2.GaussianBlur(normal,(5,5),0)
    otsu = cv2.GaussianBlur(otsu,(5,5),2)

    cv2.adaptiveThreshold(imgray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2,adaptive);

    '''
    cv2.threshold(imgray,rakam,255,cv2.THRESH_BINARY_INV,normal)

    cv2.threshold(imgray,rakam,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU,otsu)

    cv2.imshow('adaptive',adaptive)

    cv2.imshow('image',imgray)
    cv2.imshow('normal',normal)
    cv2.imshow('otsu',otsu)
    '''

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    #cv2.imshow('s',hsv[:,:,1])

    s=hsv[:,:,1]
    bos=hsv.copy()
    bos[:,:,:]=0
    s = cv2.GaussianBlur(s,(5,5),10)
    otsu_s=s.copy()
    normal_s=s.copy()
    cv2.threshold(s,rakam,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU,otsu_s)

    otsu_s2=otsu_s.copy()
    contours, hierarchy = cv2.findContours(otsu_s2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.imshow('s_adaptive',otsu_s)

    index=np.zeros(len(contours),int)

    for a in range(0,len(contours)):
        index[a]=len(contours[a])

    cnt = contours[index.argmax()]

    cv2.drawContours(bos, [cnt], 0, (0,255,0), 3)

    cv2.imshow("Contour",bos)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break