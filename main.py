from getPokemon import *
from presentacion import *
from simulador import *
from getStrategy import *
import os

IA = getIA()
Teams = []
Teams.append(getEquipo1())
Teams.append(getEquipo2())
Teams.append(getEquipo3())

strategy = {"water": " ", "normal": " ", "bug": " "}
for i in strategy:
	strategy[i] = startStrategy(i)

a=True

while a:
	os.system('clear')
	choice = int(presentacion())
	choice = choice-1
	os.system('clear')

	win = simulacion(IA,Teams[choice], strategy)
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
		IA = getIA()
		Teams = []
		Teams.append(getEquipo1())
		Teams.append(getEquipo2())
		Teams.append(getEquipo3())
	else:
		a=False

	


