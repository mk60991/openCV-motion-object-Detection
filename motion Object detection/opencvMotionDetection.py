# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 13:53:28 2018

@author: hp
"""

import numpy as np
import cv2

#read live video stream from webcam
#in our case my camera support '0' instead of '1'
cap=cv2.VideoCapture(0)
#to read video from given 'filename'
#cap=cv2.VideoCapture("motion.mp4")

#adjust 'width' of video
cap.set(3,640)
#adjust height of video
cap.set(4,480)

#extract the moving foreground from static background
#algorithhm used: Gaussian mixture background/foreground segmentation algorithm
fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
    #video read frame by frame
    #grab,decodes and returns the next video frame
    ret,frame=cap.read()
    #captured frame by camera, read it 
    #and apply above algorithm ,finally motion is extracted from the video
    videoMasked=fgbg.apply(frame)
    #to show real video from camera
    cv2.imshow('original',frame)
   #to show masked video on camera
    cv2.imshow('masked',videoMasked)
    
  
    
    if cv2.waitKey(1) & 0XFF==ord('q'):
        
        break
cap.release()
cv2.destroyAllWindows()