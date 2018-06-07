def func():
	print ("func() in one.py")
print("***this is one.py****")
print("nameis :"+__name__)
if __name__=="__main__":
	print("one.py is being run directly")
else:
	print("one.py is imported into another module")