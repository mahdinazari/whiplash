class Washing: 
	def wash(self): 
		print("Washing...") 


class Rinsing: 
	def rinse(self): 
		print("Rinsing...") 


class Spinning: 
	def spin(self): 
		print("Spinning...") 


class WashingMachine: 
	'''Facade'''

	def __init__(self): 
		self.washing = Washing() 
		self.rinsing = Rinsing() 
		self.spinning = Spinning() 

	def startWashing(self): 
		self.washing.wash() 
		self.rinsing.rinse() 
		self.spinning.spin() 


if __name__ == "__main__": 

	washingMachine = WashingMachine() 
	washingMachine.startWashing() 
