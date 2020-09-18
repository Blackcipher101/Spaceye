import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('09-16 13:19:06.jpg',0)
#current = cv2.imread('Cstar.png')
blur = cv2.GaussianBlur(img,(35,35),0)
previousimg = cv2.imread('09-16 13:19:06.jpg')
img1 = cv2.imread('09-16 13:19:06.jpg',1)
ret,thresh = cv2.threshold(blur,20,255,0)
thresh1 =cv2.bitwise_not(thresh)
contours,hierarchy = cv2.findContours(thresh1, 1, 2)

cnt = contours[0]
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])


filename = '09-16 13:19:06.jpg'
img2 = cv2.imread(filename)
gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.4)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
img2[res[:,1],res[:,0]]=[0,0,255]
img2[res[:,3],res[:,2]] = [0,255,0]

filename = '09-16 13:19:06next.jpg'
img2 = cv2.imread(filename)
gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.4)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
img2[res[:,1],res[:,0]]=[0,0,255]
img2[res[:,3],res[:,2]] = [0,255,0]
t=input("input time gap")
time= t*

print leftmost,' ',rightmost,' ',topmost,' ',bottommost
img1 = cv2.circle(img1,leftmost, 12, (0,255,255), -1)
img1 = cv2.circle(img1,rightmost, 12, (0,255,255), -1)
img1 = cv2.circle(img1,topmost, 12, (0,255,255), -1)
img1 = cv2.circle(img1,bottommost, 12, (0,255,255), -1)




cv2.imshow("images",img2)
cv2.imshow("image06",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
