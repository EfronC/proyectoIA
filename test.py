from decision import decision
import pykemon
from getType import getType
from movimiento import getMovimiento
from batalla import *
from getElement import *

p=pykemon.get(pokemon="charizard")
q=pykemon.get(pokemon="poliwrath")

class Charizard():
	name=p.name
	attack=p.attack
	defense=p.defense
	speed=p.speed
	hp=(p.hp)*10
	tipo=getType(p.types)
	mov1=getMovimiento(332,"Flying")#60
	mov2=getMovimiento(231,"Steel")#100
	mov3=getMovimiento(53,"Fire")#95
	mov4=getMovimiento(14,"Normal")#UpAttack


class Poliwrath():
	name=q.name
	attack=q.attack
	defense=q.defense
	speed=q.speed
	hp=(q.hp)*10
	tipo=getType(q.types)
	mov1=getMovimiento(398,"Poison")#80
	mov2=getMovimiento(280,"Figthing")#75
	mov3=getMovimiento(8,"Ice")#75
	mov4=getMovimiento(57,"Water")#95

prueba = Charizard()
prueba2 = Poliwrath()

a = getElement(prueba.mov3.tipo,prueba2.tipo)
print a

