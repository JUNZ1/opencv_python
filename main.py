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
cap = cv2.VideoCapture(0)


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

ax = fig.add_subplot(121)

a=ax.imshow(img,cmap = 'gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

bx = fig.add_subplot(122)
b=bx.imshow(imgray,cmap = 'gray')
plt.title('Edge Image')
plt.xticks([])
plt.yticks([])


while(True):


    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    img = cv2.cvtColor(frame,0)


    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    a.set_data(imgray)
    b.set_data(img)
    plt.draw()
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break