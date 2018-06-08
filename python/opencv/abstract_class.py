'''from abc import ABC,abstractmethod

class Restaurant(ABC):
	@abstractmethod
	def dinninghall(self):
		pss
class FiveStar(Restaurant):
	def swimmingpool(self):
		print ("yes,there is a swimming pool")

class BeachsideResort(Restaurant):
	def beachsidecafe(self):
		print ("yes, there is a beachside cafe")

fs= FiveStar()
fs.swimmingpool()

bc= BeachsideResort()
bc.beachsidecafe()    ####it will give u an error like 
##TypeError: Can't instantiate abstract class FiveStar with abstract methods dinninghall  '''



from abc import ABC,abstractmethod

class Restaurant(ABC):
	@abstractmethod
	def dinninghall(self):
		pass
class FiveStar(Restaurant):
	def swimmingpool(self):
		print ("\nyes,there is a swimming pool")
	def dinninghall(self):
		print("dining hall has 100 PAX capacity in five star restaurant\n")

class BeachsideResort(Restaurant):
	def beachsidecafe(self):
		print ("yes, there is a beachside cafe")
	def dinninghall(self):
		print("dining hall has 200 PAX capacity in beach side resort\n")


fs= FiveStar()
fs.swimmingpool()
fs.dinninghall()

bc= BeachsideResort()
bc.beachsidecafe() 
bc.dinninghall()


''' it will give output as 
yes,there is a swimming pool
dining hall has 100 PAX capacity in five star restaurant

yes, there is a beachside cafe
dining hall has 200 PAX capacity in beach side resort'''