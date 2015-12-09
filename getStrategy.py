import itertools

def startStrategy(element):
	a = [0,1,2,3]
	b = list(itertools.permutations(a,2))

	class strategy:
		bad = []
		tryAnother = False
		util = []
		mix = a+b
		def __init__(self, element):
			if element=="water": 
				self.util.append(1)
			elif element=="normal": 
				self.util.append(1)
			else: 
				self.util.append(2)

			self.mix.remove(self.util[0])

	x = strategy(element)

	return x

def getStrategy(element, strategy):
	if not(strategy.tryAnother):
		return strategy.util[0]
	strategy.bad.append(strategy.util[0])
	del strategy.util[0]

	strategy.util.append(strategy.mix[0])
	return strategy.util[0] 


