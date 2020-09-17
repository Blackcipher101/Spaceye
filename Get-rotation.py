import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('09-16 13:19:06.jpg',0)
#current = cv2.imread('Cstar.png')
previousimg = cv2.imread('09-16 13:19:06.jpg')
img1 = cv2.imread('09-16 13:19:06.jpg',1)
ret,thresh = cv2.threshold(img,20,255,0)
thresh1 =cv2.bitwise_not(thresh)
contours,hierarchy = cv2.findContours(thresh1, 1, 2)

cnt = contours[0]
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
print leftmost,' ',rightmost,' ',topmost,' ',bottommost
img1 = cv2.circle(img1,leftmost, 12, (0.255,255), -1)
img1 = cv2.circle(img1,rightmost, 12, (0,255,255), -1)
img1 = cv2.circle(img1,topmost, 12, (0,255,255), -1)
img1 = cv2.circle(img1,bottommost, 12, (0,255,255), -1)




cv2.imshow("images",thresh)
cv2.imshow("image06",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
