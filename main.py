from getPokemon import *
from presentacion import *
from simulador import *

IA = getIA()
aux=IA
Teams = []
Teams.append(getEquipo1())
Teams.append(getEquipo2())
Teams.append(getEquipo3())
aux2=Teams

a=True

while a:
	choice = int(presentacion())
	choice = choice-1

	win = simulacion(IA,Teams[choice])
	if win == 1:
		print "*************************************"
		print "IA gana"

	else:
		print "*************************************"
		print "Jugador gana"
	print "**************************************"
	des = raw_input("Desea jugar otra partida[Y-N]")
	if des == 'Y':
		a=True
	else:
		a=False

	#IA=aux
	#Teams=aux2


