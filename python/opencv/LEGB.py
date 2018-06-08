# LOCAL-> ENCLOSED -> GLOBAL ->BUILT-INS

i=1
def A():
	i=5
	print ("im local i=",i)
print("im global i=",i)

A()


