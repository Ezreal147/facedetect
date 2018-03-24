import cv2
import os
from PIL import Image
camera=cv2.VideoCapture(0)
camera.set(3,640)
camera.set(4,480)
recognizer=cv2.face.LBPHFaceRecognizer_create()
faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
facecascade.load('/home/pi/facedetect/haarcascade_frontalface_default.xml')
count=0
face_id=input('\n enter user id end press <return> -->')
while True:
	ret,frame=camera.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.2,
		minNeighbors=5,
		minSize=(20,20)
	)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		count+=1
		cv2.imwrite('dataset/User.'+str(face_id)+'.'+str(count)+'.jpg',gray[y:y+h,x:x+w])
	cv2.imshow('image', frame)
	if cv2.waitKey(10) & 0xff==27:
		break
	elif count>=30:
		break
camera.release()
cv2.destroyAllWindows()
