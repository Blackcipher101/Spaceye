import cv2
import numpy as np
from matplotlib import pyplot as plt

Gstar=cv2.imread("Gstar.png")
Astar=cv2.imread("Astar.png")
Kstar=cv2.imread("Kstar.png")
Ostar=cv2.imread("Ostar.png")
Fstar=cv2.imread("Fstar.png")
Mstar=cv2.imread("M.png")
Bstar=cv2.imread("Bstar.png")
tempG1=Gstar[:,20:300,:]
print tempG1.shape
w, h = 280,181

tempG2=Gstar[:,500:600,:]
tempA1=Astar[:,20:300,:]
tempA2=Astar[:,500:600,:]
tempF1=Fstar[:,20:300,:]
tempF2=Fstar[:,500:600,:]
tempO1=Ostar[:,20:300,:]
tempO2=Ostar[:,500:600,:]
tempM1=Mstar[:,20:300,:]
tempM2=Mstar[:,500:600,:]
tempB1=Bstar[:,20:300,:]
tempB2=Bstar[:,500:600,:]
methods = ['cv2.TM_CCOEFF_NORMED',]

for meth in methods:
    img = Gstar.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,tempG1,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print min_val,' ',max_val
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    Gstar=cv2.rectangle(Gstar,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
cv2.imshow("img",Gstar)
cv2.waitKey(0)
