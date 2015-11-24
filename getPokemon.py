import pykemon
from getType import getType
from movimiento import getMovimiento
p=pykemon.get(pokemon="charizard")#6
q=pykemon.get(pokemon="poliwrath")#62
r=pykemon.get(pokemon="snorlax")#143
s=pykemon.get(pokemon="scyther")#123

def getIA():
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

	return Charizard

def getEquipo1():
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
	return Poliwrath

def getEquipo2():
	class Snorlax():
		name=r.name
		attack=r.attack
		defense=r.defense
		speed=r.speed
		hp=(r.hp)*10
		tipo=getType(r.types)
		mov1=getMovimiento(428,"Psychic")#80
		mov2=getMovimiento(242,"Dark")#80
		mov3=getMovimiento(247,"Ghost")#80
		mov4=getMovimiento(157,"Rock")#75
	return Snorlax

def getEquipo3():
	class Scyther():
		name=s.name
		attack=s.attack
		defense=s.defense
		speed=s.speed
		hp=(s.hp)*10
		tipo=getType(s.types)
		mov1=getMovimiento(404,"Bug")#80
		mov2=getMovimiento(403,"Flying")#75
		mov3=getMovimiento(249,"Rock")#40
		mov4=getMovimiento(38,"Normal")#120
	return Scyther