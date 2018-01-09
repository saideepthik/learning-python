#creating slide bar to adjust the hsv values of an image manually 
import cv2
import numpy as np


#cap = cv2.VideoCapture("challenge.mp4")
#cap.set(cv2.CAP_PROP_FPS, 10);
#frame_count=0
def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')
frame1=cv2.imread("frame152.jpg")
# Starting with 100's to prevent error while masking
h,s,v = 0,0,0

# Creating track bar
cv2.createTrackbar('h', 'result',0,179,nothing)
cv2.createTrackbar('l', 'result',0,255,nothing)
cv2.createTrackbar('s', 'result',0,255,nothing)
i=0
while(1):
	frame=frame1.copy()
	#ret , frame = cap.read()
	#if ret:

	#cv2.imwrite("test/frame"+str(i)+".jpg",frame)
	#i=i+1
	#converting to HSV
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)

	# get info from track bar and appy to result
	h = cv2.getTrackbarPos('h','result')
	l = cv2.getTrackbarPos('l','result')
	s = cv2.getTrackbarPos('s','result')

	# Normal masking algorithm
	lower_blue = np.array([h,l,s])
	upper_blue = np.array([255,255,255])

	mask = cv2.inRange(hsv,lower_blue, upper_blue)

	result = cv2.bitwise_and(frame,frame,mask = mask)

	cv2.imshow('result',result)
	#else :pass
		#cap.set(cv2.CAP_PROP_POS_FRAMES, 0)


	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cap.release()
