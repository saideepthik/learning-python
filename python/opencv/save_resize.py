import numpy as np
import cv2
def nothing(x):
    pass

num=0

cap = cv2.VideoCapture(0)


while 1:

	ret, img = cap.read()

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	# add this

	dim = (300,300)
	frame = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

	cv2.imshow("resized", frame)
	cv2.imwrite('pics'+str(num)+'.jpg', frame)
        num=num+1
	print "saved"
	#i+=1

	if cv2.waitKey(25) & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()
