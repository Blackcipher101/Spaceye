import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('Astar.png')
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
H=[]
Fe=[]
Mn=[]
He=[]
Heion=[]
CN=[]
Na=[]
TiO=[]
CaH=[]
dopplershift=0
for i in range(len(adlinesfinal)):
    wavelenght=((end-start)*adlinesfinal[i])/int(img1.shape[1])
    wavelenght+=start
    wavelength.append(wavelenght)
for i in range(len(wavelength)):
    if wavelength[i]<=660 and wavelength[i]>=652: #656
        H.append(wavelength[i])
    if wavelength[i]<=408 and wavelength[i]>=400: #404.5
        Fe.append(wavelength[i])
        Mn.append(wavelength[i])
    if wavelength[i]<=425 and wavelength[i]>=417:
        He.append(wavelength[i])
    if wavelength[i]<=444 and wavelength[i]>=434:
        Heion.append(wavelength[i])
    if wavelength[i]<=429 and wavelength[i]>=421:
        CN.append(wavelength[i])
    if wavelength[i]<=593 and wavelength[i]>=585:
        Na.append(wavelength[i])
    if wavelength[i]<=635 and wavelength[i]>=629:
        TiO.append(wavelength[i])
    if wavelength[i]<=639 and wavelength[i]>=633:
        CaH.append(wavelength[i])
val=max(len(CaH),len(H),len(Fe),len(Heion),len(CN),len(Na),len(TiO))
if val==len(TiO):
    avg=sum(TiO)/len(TiO)
    dopplershift=(avg-632)/632
if val==len(H):
    avg=sum(H)/len(H)
    dopplershift=(avg-656.3)/656.3
if val==len(He):
    avg=sum(He)/len(He)
    dopplershift=(avg-421)/421
if val==len(Fe):
    avg=sum(Fe)/len(Fe)
    dopplershift=(avg-404.5)/404.5
if val==len(Heion):
    avg=sum(Heion)/len(Heion)
    dopplershift=(avg-440)/440
if val==len(Na):
    avg=sum(Na)/len(Na)
    dopplershift=(avg-588.9)/588.9
if val==len(CaH):
    avg=sum(CaH)/len(CaH)
    dopplershift=(avg-634)/634
if val==len(CN):
    avg=sum(CN)/len(CN)
    dopplershift=(avg-420)/420
print dopplershift
c=300000000
vs=c*dopplershift
print vs
cv2.imshow("graph",specgraph)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
