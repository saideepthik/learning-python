myfile1=open("myfile.txt","w")
myfile1.write("banglore is a beautifull city."+"\n"+"i love the traffic!!!")
myfile1.close() 

myfile1=open("myfile.txt","r+")
myfile1.write("hi there!")

print (myfile1.read(100))
myfile1.close()

with open('myfile.txt','w') as f:
	f.write("hi there!")

f=open("myfile.txt","r+")
print (f.read(100))
myfile1.close()