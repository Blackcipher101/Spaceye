import cv2
import numpy as np
from matplotlib import pyplot as plt


star=cv2.imread("M.png")
Gstar=cv2.imread("Gstar.png")
Astar=cv2.imread("Astar.png")
Kstar=cv2.imread("Kstar.png")
Ostar=cv2.imread("Ostar.png")
Fstar=cv2.imread("Fstar.png")
Mstar=cv2.imread("M.png")
Bstar=cv2.imread("Bstar.png")
tempG1=Gstar[20:140:,20:300,:]
tempG2=Gstar[20:140:,500:600,:]
tempA1=Astar[20:140,20:300,:]
tempA2=Astar[20:140:,500:600,:]
tempF1=Fstar[20:140:,20:300,:]
tempF2=Fstar[20:140:,500:600,:]
tempO1=Ostar[20:140:,20:300,:]
tempO2=Ostar[20:140:,500:600,:]
tempM1=Mstar[20:140:,20:300,:]
tempM2=Mstar[20:140:,500:600,:]
tempB1=Bstar[20:140,20:300,:]
tempB2=Bstar[20:140:,500:600,:]
tempK1=Kstar[20:140:,20:300,:]
tempK2=Kstar[20:140:,500:600,:]
method = 'cv2.TM_CCOEFF_NORMED'
method = eval(method)

# Apply template Matching
resG1 = cv2.matchTemplate(star,tempG1,method)
min_val, max_valG1, min_loc, max_loc = cv2.minMaxLoc(resG1)
resG2 = cv2.matchTemplate(star,tempG2,method)
min_val, max_valG2, min_loc, max_loc = cv2.minMaxLoc(resG2)
resA1 = cv2.matchTemplate(star,tempA1,method)
min_val, max_valA1, min_loc, max_loc = cv2.minMaxLoc(resA1)
resA2 = cv2.matchTemplate(star,tempA2,method)
min_val, max_valA2, min_loc, max_loc = cv2.minMaxLoc(resA2)
resM1 = cv2.matchTemplate(star,tempM1,method)
min_val, max_valM1, min_loc, max_loc = cv2.minMaxLoc(resM1)
resM2 = cv2.matchTemplate(star,tempM2,method)
min_val, max_valM2, min_loc, max_loc = cv2.minMaxLoc(resM2)
resF1 = cv2.matchTemplate(star,tempF1,method)
min_val, max_valF1, min_loc, max_loc = cv2.minMaxLoc(resF1)
resF2 = cv2.matchTemplate(star,tempF2,method)
min_val, max_valF2, min_loc, max_loc = cv2.minMaxLoc(resF2)
resO1 = cv2.matchTemplate(star,tempO1,method)
min_val, max_valO1, min_loc, max_loc = cv2.minMaxLoc(resO1)
resO2 = cv2.matchTemplate(star,tempO2,method)
min_val, max_valO2, min_loc, max_loc = cv2.minMaxLoc(resO2)
resB1 = cv2.matchTemplate(star,tempB1,method)
min_val, max_valB1, min_loc, max_loc = cv2.minMaxLoc(resB1)
resB2 = cv2.matchTemplate(star,tempB2,method)
min_val, max_valB2, min_loc, max_loc = cv2.minMaxLoc(resB2)
resK1 = cv2.matchTemplate(star,tempK1,method)
min_val, max_valK1, min_loc, max_loc = cv2.minMaxLoc(resK1)
resK2 = cv2.matchTemplate(star,tempK2,method)
min_val, max_valK2, min_loc, max_loc = cv2.minMaxLoc(resK2)


top_left = max_loc
#bottom_right = (top_left[0] + w, top_left[1] + hA1)

if max_valG1 + max_valG2  >=1.999:
    print "G"
    print "1.4 to 2.1 times the mass of the Sun surface temperatures between 7600 and 10,000 K"



if max_valA1 + max_valA2  >=1.999:
    print "A1"
    print ""

if max_valM1 + max_valM2  >=1.999:
    print "M1"
    print "	2,400–3,700 K	0.08–0.45 sun mass""


if max_valF1 + max_valF2  >=1.999:
    print "F1"
    print "	6,000–7,500 K 1.04–1.4 sun mass"


if max_valO1 + max_valO2  >=1.999:
    print "O1"
    print "temperatures in excess of 30,000 kelvin O-type stars range from 10,000 times the Sun to around 1,000,000 times, giants from 100,000 times the Sun to over 1,000,000, and supergiants from about 200,000 times the Sun to several million times"


if max_valB1 + max_valB2  >=1.999:
    print "B1"
    print " to 16 times the mass of the Sun surface temperatures between 10,000 and 30,000 K"

if max_valK1 + max_valK2  >=1.999:
    print "K1"
    print "3,700–5,200 K 0.45–0.8 sun mass"
