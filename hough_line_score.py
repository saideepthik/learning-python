import cv2
import numpy as np
import os


image=cv2.imread("index1.png")
r = 500.0 / image.shape[1]
dim = (500, int(image.shape[0] * r))
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
gray= cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

canny_edges = cv2.Canny(gray, 50, 150)

cv2.imshow('canny',canny_edges)

try:	
	lines = cv2.HoughLinesP(canny_edges, 1, np.pi/90, 30,1, 200)
	cnt=1
	for line in lines:
		print cnt
		cnt+=1
		
	cv2.imshow('final',result)

except: pass

cv2.waitKey(0)
cv2.destroyAllWindows()
