class A1():
	def who_am_i(self):
		print("i'm A1")
	pass

class A2():
	def who_am_i(self):
		print("i'm A2")

class A3():
	def who_am_i(self):
		print("i'm A3")


class B(A1,A2):
	#def who_am_i(self):
		#print("i'm B")
	pass

class C(A3):
	def who_am_i(self):
		print("i'm C")


class D(B,C):
	#def who_am_i(self):
		#print("i'm D")
	pass

d1=D()
d1.who_am_i()

c1=C()
c1.who_am_i()



# check for different outputs by comment and un comment piece of code to get the tree of multiple inheritance




