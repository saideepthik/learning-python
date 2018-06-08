'''a_var = 'globalvalue'

def outer():
	a_var = 'enclosedvalue'

	def inner():
		a_var = 'local value'      #it will give local
		print(a_var)
	inner()

outer()'''


'''a_var = 'globalvalue'

def outer():
	a_var = 'enclosedvalue'         #it will give enclosed value

	def inner():
		#a_var = 'local value'  
		print(a_var)
	inner()

outer()'''


i=1
def A():
	i=5
	print ("im local i=",i)
	def B():
		nonlocal i
		print ("im non-local i=",i)
		i=6
		print("iam the new i=",i)
	B()
print ("iam the global i=",i)

A()


''' output: iam the global i= 1
im local i= 5
im non-local i= 5
iam the new i= 6 '''
