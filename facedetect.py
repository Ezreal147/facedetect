import cv2
faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def facedetect(trump):
	# trump=cv2.imread(img)
	# height=trump.shape[0]
	# width=trump.shape[1]
	# beishu=height/350
	# trump=cv2.resize(trump,(int(width/beishu),int(height/beishu)),interpolation=cv2.INTER_CUBIC)
	# print(trump.shape)
	gray_trump=cv2.cvtColor(trump,cv2.COLOR_BGR2GRAY)
	faces=faceCascade.detectMultiScale(
		gray_trump,
		scaleFactor=1.2,
		minNeighbors=5,
		minSize=(20,20)
	)
	for (x,y,w,h) in faces:
		cv2.rectangle(trump,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray=gray_trump[y:y+h,x:x+w]
		roi_color=trump[y:y+h,x:x+w]
		return trump
if __name__ == '__main__':
	for i in range(0,4):
		facedetect('zzz'+str(i)+'.jpg',i)
	cv2.waitKey(4000)