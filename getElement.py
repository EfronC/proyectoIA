import pykemon

#FLying - 3
#Steel - 9
#Fire - 10
#Normal - 1
#Poison - 4
#Figthing - 2
#Ice - 15
#Water - 11
#Psychic - 14
#Dark - 17
#Ghost - 8
#Rock - 6
#Bug - 7

def getElement(T1,T2):
	Elementos={
	"flying":3,
	"steel":9,
	"fire":10,
	"normal":1,
	"poison":4,
	"figthing":2,
	"ice":15,
	"water":11,
	"psychic":14,
	"dark":17,
	"ghost":8,
	"rock":6,
	"bug":7
	}

	el1 = pykemon.get(type_id=Elementos[T1.lower()])
	el2 = pykemon.get(type_id=Elementos[T2.lower()])

	if el2.name.lower() in el1.super_effective:
		return "weak"
	elif el2.name.lower() in el1.ineffective:
		return "strong"
	else:
		return "normal"