from decision import *
from conclusion import *
from batalla import *
from getStrategy import *
import os

def simulacion(IA,Team, strategy):
	a=True

	while a:
		mov=decision(Team,IA)
		mov=mov-1
		os.system('clear')
		des = getStrategy(Team.tipo, strategy[Team.tipo])
		if des==list():
			des = des[0][0]
		res=batalla(mov,IA,Team, des)
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

	