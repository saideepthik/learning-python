class Error(Exception):
	pass
class SmallNumber(Error):
	def raiseexception(self):
		print("Hi, you are inside SmallNumberClass")


class LargeNumber(Error):
	def raiseexception(self):
		print("Hi, you are inside SmallNumberClass")
number = 15

while True:
	try:
		num=int(input("enter a number:"))
		if num < number:
			raise SmallNumber
		elif num>number:
			raise LargeNumber
		break
	except SmallNumber:
		print("this value is too small,try again!")
		k= SmallNumber()
		k.raiseexception()
	except LargeNumber:
		print("this value is too large,try again!")
		k= LargeNumber()
		k.raiseexception()
print("Congratulations! Your guess is right.")