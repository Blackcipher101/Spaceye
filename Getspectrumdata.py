import cv2
import numpy as np
from matplotlib import pyplot as plt
def spectrum(filename):
    print("reached")
    print(filename)
    img = cv2.imread(filename)
    specgraph = np.zeros(img.shape, np.uint8)
    print(img.shape[1])
    print()
    for i in range (img.shape[1]):
        print(i)
        redval=img[int(img.shape[0]/2)][i][2]
        redhieght=(redval*181)/255
        greenval=img[int(img.shape[0]/2)][i][1]
        greenhieght=(greenval*181)/255
        blueval=img[int(img.shape[0]/2)][i][0]
        bluehieght=(blueval*181)/255
        specgraph = cv2.circle(specgraph,(i,int(181-redhieght)), 1, (0,0,255), -1)
        specgraph = cv2.circle(specgraph,(i,int(181-greenhieght)), 1, (0,255,0), -1)
        specgraph = cv2.circle(specgraph,(i,int(181-bluehieght)), 1, (255,0,0), -1)
    print("reached")
    return specgraph
