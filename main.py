from __future__ import division
import numpy as np
import cv2
from matplotlib import pyplot as plt
from time import *

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


pardus=cv2.imread('pardus.jpg')
pardus = cv2.cvtColor(pardus,0)
pardus = cv2.resize(pardus, (640, 480))

boxes = []
global crop
crop = cv2.resize(pardus, (640, 480))

def on_mouse(event, x, y, flags, params):
    # global img


    if event == cv2.EVENT_LBUTTONDOWN:
         print 'Start Mouse Position: '+str(x)+', '+str(y)
         sbox = [x, y]
         boxes.append(sbox)
         # print count
         # print sbox

    elif event == cv2.EVENT_LBUTTONUP:
        print 'End Mouse Position: '+str(x)+', '+str(y)
        ebox = [x, y]
        boxes.append(ebox)
        print boxes
        try:
            global crop
            crop = img[boxes[-2][1]:boxes[-1][1],boxes[-2][0]:boxes[-1][0]]

        except cv2.error:
            return





cv2.namedWindow('image')
cv2.createTrackbar('sayi1', 'image',1,255,nothing)
cv2.createTrackbar('sayi2', 'image',1,255,nothing2)
cv2.setMouseCallback('image', on_mouse, 0)


cap = cv2.VideoCapture(1)


while(True):

    try:
        template=cv2.imread('Crop2.jpg')
        cv2.imshow('template',template)
        [z, w, h] = template.shape[::-1]
        print h,z,w
    except cv2.error:
            pass

    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    img = cv2.cvtColor(frame,1)

    yak1=img.copy()
    yak2=img.copy()
    yak3=img.copy()
    yak4=img.copy()
    yak5=img.copy()
    yak6=img.copy()


    #zeros = np.zeros(img.shape, dtype=np.uint8)

    #Yaklasim 1
    res1 = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res1)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(yak1,top_left, bottom_right, 255, 2)


    #Yaklasim 2
    res2 = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res2)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(yak2,top_left, bottom_right, 255, 2)

    #Yaklasim 3
    res3 = cv2.matchTemplate(img,template,cv2.TM_CCORR)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res3)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(yak3,top_left, bottom_right, 255, 2)

    #Yaklasim 4
    res4 = cv2.matchTemplate(img,template,cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res4)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(yak4,top_left, bottom_right, 255, 2)


    #Yaklasim 5
    res5 = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res5)
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(yak5,top_left, bottom_right, 255, 2)


    #Yaklasim 6
    res6 = cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res6)
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(yak6,top_left, bottom_right, 255, 2)



    cv2.imshow('image',img)

    cv2.imshow('yak1',yak1)
    cv2.imshow('sonuc1',res1)

    cv2.imshow('yak2',yak2)
    cv2.imshow('sonuc2',res2)

    cv2.imshow('yak3',yak3)
    cv2.imshow('sonuc3',res3)

    cv2.imshow('yak4',yak4)
    cv2.imshow('sonuc4',res4)

    cv2.imshow('yak5',yak5)
    cv2.imshow('sonuc5',res5)

    cv2.imshow('yak6',yak6)
    cv2.imshow('sonuc6',res6)

    #print res1
    k = cv2.waitKey(33)
    if k==1048689:    # 'q' tusu cikmak icin
        break
    elif k==-1:  # gerekiyor
        continue
    elif k==1048691:  # 's' tusu kaydediyor
        cv2.imwrite('Crop2.jpg',crop)
        print 'goruntu kaydedildi'