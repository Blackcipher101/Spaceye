import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('Gstar.png')
img=cv2.medianBlur(img1,7)
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
print hsv.shape
#cv2.namedWindow('img', cv2.WINDOW_NORMAL)
#cv2.namedWindow('graph', cv2.WINDOW_NORMAL)
print "starting frequency"
start=input()
print "Final frequency"
end=input()
adlinesfinal=[]
specgraph = np.zeros(img.shape, np.uint8)
adred=[]
adblue=[]
adgreen=[]
wavelength=[]
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

for i in range (2,img.shape[1]-2):
    if i in adgreen and i in adred:
        adlinesfinal.append(i)
    if i in adgreen and i in adblue:
        adlinesfinal.append(i)
    if i in adblue and i in adred:
        adlinesfinal.append(i)
    if (img[0,i,2]+img[0,i,1])<10 and i in adblue:
        adlinesfinal.append(i)
    if (img[0,i,0]+img[0,i,1])<10 and i in adred:
        adlinesfinal.append(i)
    if (img[0,i,2]+img[0,i,0])<10 and i in adgreen:
        adlinesfinal.append(i)
H=0
Fe=0
Mn=0
He=0
Heion=0
CN=0
Na=0
TiO=0
CaH=0
for i in range(len(adlinesfinal)):
    wavelenght=((end-start)*adlinesfinal[i])/int(img1.shape[1])
    wavelenght+=start
    print wavelenght,' ',adlinesfinal[i]
    wavelength.append(wavelenght)

for i in range(len(wavelength)):
    if wavelength[i]<=661 and wavelength[i]>=649: #656
        H+=1
        print(H)
    if wavelength[i]<=409 and wavelength[i]>=400: #404.5
        Fe+=1
        Mn+=1
    if wavelength[i]<=425 and wavelength[i]>=415:
        He+=1
    if wavelength[i]<=445 and wavelength[i]>=435:
        Heion+=1
    if wavelength[i]<=430 and wavelength[i]>=420:
        CN+=1
    if wavelength[i]<=594 and wavelength[i]>=584:
        Na+=1
    if wavelength[i]<=634 and wavelength[i]>=624:
        TiO+=1
    if wavelength[i]<=639 and wavelength[i]>=632:
        CaH+=1
if  H>=2:
    print"Hydogen present"
if  He>=2:
    print"Helium present"
if  Fe>=2:
    print "Iron present"
if  Mn>=2:
    print "Mn present"
if  Heion>=2:
    print"Helium ion present"
if  CN>=2:
    print "CN radical present"

if  TiO>=2:
    print "TiO present"
if CaH>=2:
    print "CaH present"

cv2.imshow("graph",specgraph)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
