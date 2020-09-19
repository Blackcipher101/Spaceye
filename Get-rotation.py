import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
cap = cv2.VideoCapture('latest_1024_0304.mp4')

# take first frame of the video
ret,frame = cap.read()
frame = cv2.flip(frame, 0)
img=cv2.imread('latest_512_0304.jpg',0)
#current = cv2.imread('Cstar.png')
blur = cv2.GaussianBlur(img,(35,35),0)
previousimg = cv2.imread('latest_512_0304.jpg')
img1 = cv2.imread('latest_512_0304.jpg',1)
ret,thresh = cv2.threshold(blur,20,255,0)
thresh1 =cv2.bitwise_not(thresh)
contours,hierarchy = cv2.findContours(thresh1, 1, 2)
x=3.9
cnt = contours[0]
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
leftmost=(int(leftmost[0]*(x+0.1)),int(leftmost[1]*x))
rightmost=(int(rightmost[0]*(x+0.1)),int(rightmost[1]*x))
bottommost=(int(bottommost[0]*(x+0.1)),int(bottommost[1]*x))
topmost=(int(topmost[0]*(x+0.1)),int(topmost[1]*x))



print leftmost,' ',rightmost,' ',topmost,' ',bottommost
img1 = cv2.circle(img1,leftmost, 12, (0,255,255), -1)
img1 = cv2.circle(img1,rightmost, 12, (0,255,255), -1)
img1 = cv2.circle(img1,topmost, 12, (0,255,255), -1)
img1 = cv2.circle(img1,bottommost, 12, (0,255,255), -1)


# setup initial location of window
r,h,c,w = 400,100,300,100  # simply hardcoded the values
track_window = (c,r,w,h)

# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
i=1
s=0
while(1):
    ret ,frame = cap.read()
    frame = cv2.flip(frame, 0)

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        # Draw it on image
        x,y,w,h = track_window
        if s==0:
            x1,y1=x,y
            s+=1
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        img2 = cv2.circle(img2,leftmost, 12, (0,255,255), -1)
        img2 = cv2.circle(img2,rightmost, 12, (0,255,255), -1)
        img2 = cv2.circle(img2,topmost, 12, (0,255,255), -1)
        img2 = cv2.circle(img2,bottommost, 12, (0,255,255), -1)
        cv2.imshow('image',img2)
        k = cv2.waitKey(4) & 0xff
        if k == 27:
            break
    else:
        break
x2,y2=x,y
distance=math.sqrt((x1-x2)**2)
distance1=math.sqrt((leftmost[0]-rightmost[0])**2)
time=(48*distance1*3.14)/distance
print time
cv2.imshow("images",img2)
cv2.imshow("image06",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
