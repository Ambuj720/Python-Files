import cv2
import pickle
import numpy as np

cap=cv2.VideoCapture('')     #video name

while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT):    
        success,img=cap.read()
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    success,img=cap.read()
    cv2.imshow("Image",img)
    cv2.waitKey(1)
