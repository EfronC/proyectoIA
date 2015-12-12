import itertools

def startStrategy(element):
	a = [0,1,2,3]

	class strategy:
		bad = []
		tryAnother = False
		util = []
		mix = a
		buff=0
		history = []
		buffext=0
		newone=0
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

def getStrategy(element, strategy, profit):
	if not(strategy.tryAnother):
		return strategy.util[0]
	#strategy.bad.append(strategy.util[0])
	if len(strategy.util)>1:
		if profit[0]>profit[1]:
			del strategy.util[1]
		elif profit[1]>profit[0]:
			del strategy.util[0]
		else:
			if len(strategy.util)>1:
				del strategy.util[1]

	if len(strategy.mix)>0:
		strategy.util.append(strategy.mix[0])
		del strategy.mix[0]
		return strategy.util[1] 
	return strategy.util[0]


