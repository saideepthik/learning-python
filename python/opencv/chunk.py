#define the chunk size
#read the file
mychunk = 1000

#path to your image file

myimagefile = 'C:\\Users\\Public\\Pictures\\Sample Pictures\\Chrysanthemum.jpg'

#open a dummy file for dumping chunks
dummyfile= open('C:\\Users\\Public\\Pictures\\Sample Pictures\\chunkfile.txt','wb+')  # write in binary data 'wb+'

with open(myimagefile,'rb') as fileloop:
	while  True:
		#read 1000byte chunks of the image
		filelines=fileloop.read(mychunk)
		if not filelines:break
		dummyfile.write(filelines)
dummyfile.close()
#destination
#reconstruct
readdummyfile = open('C:\\Users\\Public\\Pictures\\Sample Pictures\\chunkfile.txt','rb')

#create the jpg file
with open('C:\\Users\\Public\\Pictures\\Sample Pictures\\Chrysanthemum.jpg','wb') as tempfile:
	for f in readdummyfile:
		tempfile.write(f)

readdummyfile.close()

