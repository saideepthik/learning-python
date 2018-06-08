class Book():
	#initializer
	def __init__(self,name):
		#an istance variable to hold the book's name
		self.__name=name

	#getter method
	@property
	def bookname(self):
		return self.__name

	#setter method
	@bookname.setter
	def bookname(self,new_name):
		self.__name=new_name


book1 = Book("harrypotter")
print (book1.bookname)

book1.bookname ="jungle book"
print (book1.bookname)




#output: names will be printed
