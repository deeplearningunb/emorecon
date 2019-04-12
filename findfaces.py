# -*- coding: utf-8 -*-
import cv2 

imgpath = ''
faceClassifierPath = ''

faceCascade = cv2.CascadeClassifier(faceClassifierPath)

img = cv2.imread(imgpath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    print('Desenhando')
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow("Faces found", img)
