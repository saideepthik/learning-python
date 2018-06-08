class Travel():
	def bookticket(self,lst):
		raise NotimplementedError("sub class must implement abstract method")

class BusinessTravel(Travel):
	def bookticket(self,lst):
		print ("i need to book %d tickets "%lst[0])

class PleasureTravel(Travel):
	def bookticket(self,lst):
		print("i need to book %d tickets "%lst[0])
		print("i need %d rooms in hotel"%lst[1])



l=int(input("how many tickets do you want to book? enter number tickets......"))

bt=BusinessTravel()
bt.bookticket([l])

r=int(input("how many rooms  do you want to book in hotel? enter number of rooms......"))

pt=PleasureTravel()
pt.bookticket([l,r])


'''output is like this.....
how many tickets do you want to book? enter number tickets......2
i need to book 2 tickets 
i need to book 2 tickets 
i need 3 rooms in hotel
how many rooms  do you want to book in hotel? enter number of rooms......3'''
