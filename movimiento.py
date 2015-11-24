import pykemon

def getMovimiento(nombre, element):
	mov=pykemon.get(move_id=nombre)
	class movimiento():
		damage=mov.power
		pp=mov.pp
		tipo=element
		name=mov.name
	return movimiento
