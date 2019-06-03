# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:42:25 2019

@author: Saba
"""

import cv2
import numpy as np
import imutils



cv2.namedWindow("frame")

cap = cv2.VideoCapture("back.mp4") # read video
_, first_frame = cap.read()
first_frame = imutils.resize(first_frame, width= 600)


while True:
    ret, frame = cap.read()
    
    if frame is None:
        break
    frame = imutils.resize(frame, width = 600)
    diff_frame = cv2.absdiff(frame, first_frame)
    # first change it to 1 channel
    gray_diff = cv2.cvtColor(diff_frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_diff, 20, 255, cv2.THRESH_BINARY)
    cnts , _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE ) # RETR_TREE : all contour , cv2.RETR_EXTERNAL: only external 
    
    if len(cnts)> 0: # for first frames that is black
            max_contour = sorted(cnts, key= cv2.contourArea, reverse= True)[0]
            x, y, w, h = cv2.boundingRect(max_contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))
    
    cv2.imshow("frame", frame)

    if cv2.waitKey(30) == ord('q'):                    
        break
    
cap.release()
cv2.destroyAllWindows()