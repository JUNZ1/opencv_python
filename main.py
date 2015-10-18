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



saban=cv2.imread('saban.jpg')


saban = cv2.cvtColor(saban,0)
saban = cv2.resize(saban, (640, 480))
cap = cv2.VideoCapture(1)


cv2.namedWindow('image')
cv2.createTrackbar('sayi1', 'image',1,255,nothing)
cv2.createTrackbar('sayi2', 'image',1,255,nothing2)


plt.ion()

fig = plt.figure()

# Capture frame-by-frame
ret, frame = cap.read()
# Our operations on the frame come here
img = cv2.cvtColor(frame,0)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ax = fig.add_subplot(311)

a=ax.imshow(img,cmap = 'gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

bx = fig.add_subplot(312)
b=bx.imshow(imgray,cmap = 'gray')
plt.title('Edge Image')
plt.xticks([])
plt.yticks([])

hist_full = cv2.calcHist([imgray],[0],None,[256],[0,256])
cx = fig.add_subplot(313)
c=cx.plot(hist_full)
plt.title('Histogram')
plt.xlim([0,256])
while(True):


    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    img = cv2.cvtColor(frame,0)


    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hist_full = cv2.calcHist([imgray],[0],None,[256],[0,256])

    equ = cv2.equalizeHist(imgray)
    histog1 = np.hstack((imgray,equ)) #stacking images side-by-side

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(imgray)

    histog2 = np.hstack((imgray,cl1)) #stacking images side-by-side
    a.set_data(imgray)
    b.set_data(img)
    cx.plot(hist_full)
    plt.draw()
    cx.cla()
    cv2.imshow('image',histog1)
    cv2.imshow('histog2',histog2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break