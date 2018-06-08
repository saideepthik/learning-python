'''while True:
	try:
		p=int(input("please enter an integer:"))
		break
	except:
		print("not a valid input, please try again!")

try:
	5/0
except ZeroDivisionError:
	print ("please dont divide by 0")

r=100
try:
	print("money"+r+"Available")
except TypeError:
	print("i told you this gives a Type Error")


# multiple exception handler
r=100
try:
	print("money"+r+"Available")
	5/0

except ZeroDivisionError:
	print ("please dont divide by 0")

except TypeError:
	print("i told you this gives a Type Error")

else:
	print("this is else block if try succeeds it will be executed")

finally:
	print("Thanks for attempting this session")'''

# multiple exception chaining

r=100
try:
	print("money"+r+"Available")
	5/0
except TypeError:
	print("money"+r+"Available")