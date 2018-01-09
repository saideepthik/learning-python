#learn how to resize an image and save it using opencv 
import cv2
import time

for i in range (2,85):

	print i
	img= cv2.imread('left'+str(i)+'.jpg')
	cv2.imshow('img',img)
	dim = (300, 300)
	frame = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	cv2.imwrite('left'+str(i)+'.jpg',frame)
	
	
cv2.destroyAllWindows()
