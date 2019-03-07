import numpy as np
import cv2

face_cascade =cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')



cap = cv2.VideoCapture(0)
cap.set(20,780) # set Width
cap.set(4,480) # set Height
while(True):
    ret, img = cap.read()
    img = cv2.flip(img, 1) # (-1) Flip camera vertically, (1) normal
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(
    	gray,
    	scaleFactor=1.2,
    	minNeighbors=5,
    	minSize=(20,50)
    )
    
    #cv2.imshow('frame', frame)
    #cv2.imshow('gray', gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  
    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()