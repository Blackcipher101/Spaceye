import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('Astar.png')
img=cv2.medianBlur(img1,7)
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
print hsv.shape
#cv2.namedWindow('img', cv2.WINDOW_NORMAL)
#cv2.namedWindow('graph', cv2.WINDOW_NORMAL)
adlinesfinal=[]
specgraph = np.zeros(img.shape, np.uint8)
adred=[]
adblue=[]
adgreen=[]
for i in range (3,img.shape[1]-3):
    redval=img[0,i,2]
    redhieght=(redval*181)/255
    greenval=img[0,i,1]
    greenhieght=(greenval*181)/255
    blueval=img[0,i,0]
    bluehieght=(blueval*181)/255
    redprevdif=int(img[0,i,2])-int(img[0,i-3,2])
    redaheadvdif=int(img[0,i,2])-int(img[0,i+3,2])
    greenprevdif=int(img[0,i,1])-int(img[0,i-3,1])
    greenaheadvdif=int(img[0,i,1])-int(img[0,i+3,1])
    blprevdif=int(img[0,i,0])-int(img[0,i-3,0])
    blaheadvdif=int(img[0,i,0])-int(img[0,i+3,0])

    y=0
    if redprevdif < y and redaheadvdif < y:
        adred.append(i)
        #adred.append(i+1)
        #adred.append(i+2)
        #adred.append(i-1)
        #adred.append(i-2)

    if greenprevdif < y and greenaheadvdif < y:
        adgreen.append(i)
        #adgreen.append(i+1)
        #adgreen.append(i+2)
        #adgreen.append(i-1)
        #adgreen.append(i-2)


    if blprevdif < y and blaheadvdif < y:
        adblue.append(i)
        #adblue.append(i+1)
        #adblue.append(i+2)
        #adblue.append(i-1)
        #adblue.append(i-2)

    specgraph = cv2.circle(specgraph,(i,181-redhieght), 1, (0,0,255), -1)
    specgraph = cv2.circle(specgraph,(i,181-greenhieght), 1, (0,255,0), -1)
    specgraph = cv2.circle(specgraph,(i,181-bluehieght), 1, (255,0,0), -1)
print adred
print adgreen
for i in range (2,img.shape[1]-2):
    if i in adgreen and i in adred:
        adlinesfinal.append(i)
    if i in adgreen and i in adblue:
        adlinesfinal.append(i)
    if i in adblue and i in adred:
        adlinesfinal.append(i)
for i in range(len(adlinesfinal)):
    wavelenght=((700-400)*adlinesfinal[i])/img1.shape[1]
    wavelenght+=400
    print(wavelenght, ' ', adlinesfinal[i])

cv2.imshow("graph",specgraph)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
