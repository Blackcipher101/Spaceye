import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Gstar.png')
specgraph = np.zeros(img.shape, np.uint8)
for i in range (img.shape[1]):
    redval=img[(img.shape[0]/2),i,2]
    redhieght=(redval*181)/255
    greenval=img[(img.shape[0]/2),i,1]
    greenhieght=(greenval*181)/255
    blueval=img[(img.shape[0]/2),i,0]
    bluehieght=(blueval*181)/255
    specgraph = cv2.circle(specgraph,(i,181-redhieght), 1, (0,0,255), -1)
    specgraph = cv2.circle(specgraph,(i,181-greenhieght), 1, (0,255,0), -1)
    specgraph = cv2.circle(specgraph,(i,181-bluehieght), 1, (255,0,0), -1)
cv2.imshow("graph",specgraph)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
