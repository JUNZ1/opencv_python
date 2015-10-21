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


cap = cv2.VideoCapture(0)


while(True):

    try:
        template=cv2.imread('Crop2.jpg')
        cv2.imshow('template',template)
        [z, w, h] = template.shape[::-1]
        #print h,z,w
    except cv2.error:
            pass

    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    img = cv2.cvtColor(frame,1)



    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,0,150,apertureSize = 3)



    lines = cv2.HoughLines(edges,1,np.pi/180,200)



    try:
        for rho,theta in lines[0]:
            #print '1==',rho,'2==',theta
            print 'Size==',lines.shape
            print lines,'\n\n\n\n\n'

            print 'Size2==',lines[0].shape
            print lines[0],'\n\n\n\n\n'
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    except TypeError:
            pass

    cv2.imshow('image',img)

    cv2.imshow('edge',edges)

    k = cv2.waitKey(33)
    if k==1048689:    # 'q' tusu cikmak icin
        break
    elif k==-1:  # gerekiyor
        continue
    elif k==1048691:  # 's' tusu kaydediyor
        cv2.imwrite('Crop2.jpg',crop)
        print 'goruntu kaydedildi'