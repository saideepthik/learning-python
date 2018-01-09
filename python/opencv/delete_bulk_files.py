# delete some files sequentially in bulk of files
import cv2
import os


for i in range (0,5000):
	img = cv2.imread('img'+str(i)+'.jpg') 
	if i%2==0:
		continue
	else:
		try: 
			os.remove('img'+str(i)+'.jpg')
		except: pass
# note: image name should have sequential number like this "img1.jpg" (img'+str(i)+'.jpg')
