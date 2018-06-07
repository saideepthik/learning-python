import one

print("***this is two.py****")
print("nameis :"+__name__)

if __name__=="__main__":
	print("two.py is being run directly")
else:
	print("two.py is imported into another module")
one.func()