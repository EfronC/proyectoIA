from decision import *
from conclusion import *
from batalla import *

def simulacion(IA,Team):
	a=True
	while a:
		mov=decision(Team,IA)
		mov=mov-1
		res=batalla(mov,IA,Team)
		con=conclusion(res)
		if con == 0:
			a=True
		elif con == 1:
			a=False
			return 1
		else:
			a = False
			return 2
		IA = res[0]
		Team=res[1]
	