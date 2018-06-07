import random

print ("\nim saideepthi kothapalli")

'''print ("\nlist concept\n") 
lst = [1,2,3]
print (lst)
c= [lst for x in range(1,3)]
print (c)

print ("\ntuple concept\n")
tuple = (1,2,3)
print (tuple)

print ("\nfunctions concept\n")

def sayhello(name):
	print("hello" + name)
	return
sayhello("ram")

print ("\ninner functions concept")

def sayhi(name):
	print("hi  " + name)
	
	def getaddress(name):
		print("hey",name,'!where are you from?')
	getaddress(name)
sayhi("deeps")


print ("\nreturn a functions concept")

def sayhi(name):
	print("hi  " + name)
	
	def getaddress(name):
		print("hey",name,'!where are you from?')

	return getaddress

sayhi("deeps")
address = sayhi("das")
address("sai")

print ("\nfunction passed as an argument concept")

def hi():
	return "i say hi!"
def hello():
	return "i say hello!"
def greeting(fn):
	#sorting the function in a variable
	greet= fn()
	print (greet) 

greeting(hi)
greeting(hello)

print ("\nclosure concept")

def addwith(num1):
	def addresult(num2):
		return num1+num2
	print (addresult)
	return addresult

add10 = addwith(10)

print (add10(9))

print ("\nclosure for counter concept")

def mycounter():
	num =0
	def startcount():
		nonlocal num
		num= num+1
		print ("current count is",num)
	return startcount

c1= mycounter()

print (c1())

print ("\nlambda concept")

t1=lambda p,q:p*q
print(t1(3,4))

import math
square_root = lambda x: math.sqrt(x)

check = lambda x: 'big' if x>100 else 'small'
print (check(10))

print ("\nmap concept")

lst= list(map(lambda num:num**2,[2,3,4,5]))
print (lst)

lst= list(map(lambda x,y,z:((x**2)/5+(y/z)),[5,24,6],[7,8,6],[2,1,3]))
print (lst)

print ("\n filter concept")

lst= list(filter(lambda num:num**3>100,[2,3,4,5,6]))
print (lst)

lst=["tiger","lion","zebra"]
print(list(filter(lambda x:x[0]=='z',lst)))

print(list(filter(lambda x:len(x)>4,lst)))

def test(x,y,z):
	return x*2+y*2+z*2

p=lambda a,b,c:test(a,b,c)+a*b*c
print (p(2,3,4))


def test(x,y,z):
	return x*2+y*2+z*2
m=[1,2,3]
n=[4,5,6]
o=[7,8,9]
result = list(map(lambda a,b,c:test(a,b,c)+a*b*c,m,n,o))
print (result)

print ("* argument concept")

def test(*args):
	print(args)
	for i in args:
		print (i)
test("delhi","banglore","mumbai","chennai")

def test1(*numbers):
	print(sum(numbers))
test1(20,30,40,50)

print ("\n ** keyword argument concept")
def test(**countrycapitals):
	print(countrycapitals)
	if 'india' in countrycapitals:
		print("the capital of india is {}".format(countrycapitals['india']))
	else:
		print("country not specified")
test(india ='new delhi',pakistan='islamabad')

print("get a consolidated list from a list of arguments containing lists, strings and numbers\n")


def test(*printables):
	temp =[]
	for i in printables:
		if type(i) is list:
			temp=temp+i
	return temp
print (test([1,2,3],[4,5,6],[7,8,9],"banglore",30,31,32,[10,11,12],['a','b','c']))

print("map/filter/reduce concept")

items = [1,2,3,4,5]
squared = list(map(lambda x:x**2,items))
print (squared)

print(list(filter(lambda x:x**2>50,items)))

print(" generator")
def mygen(n):
	for i in range(n):
		yield i
l=mygen(5)
for i in l:
	print (i)

def mygen(n):
	for i in range(n):
		name ='rank'+str(i)	
		yield name
l=mygen(5)
for i in l:
	print (i)'''

def enclosure(fun):
	def wrapper(x):
		print("this line is printed before executing your function")
		fun(x)
		print("this line is printed after executing your function")
	return wrapper

@enclosure
def addonetonumber(n):
	k=n+1
	print (k)

@enclosure
def multiplywith7(n):
	k=n*7
	print (k)

addonetonumber(52)
multiplywith7(4)













