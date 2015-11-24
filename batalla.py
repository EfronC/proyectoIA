import random
from getElement import *
#Damage=(attack+damage-defense)resistance

def getForm(tipo,at,tar, dam):
	forms={
	"strong":int((dam+at.attack-tar.defense)*0.5),
	"normal":int(dam+at.attack-tar.defense),
	"weak":int((dam+at.attack-tar.defense)*2)
	}

	return forms[tipo]

def isNotDead(per):
	if per.hp>0:
		return True
	return False

def batalla(mov,IA,Team):
	des=random.randint(0,3)
	if IA.speed>Team.speed:
		if des == 0:
			res = getElement(IA.mov1.tipo,Team.tipo)
			damage=getForm(res,IA,Team,IA.mov1.damage)
			Team.hp=Team.hp-damage
			juego = "IA uso "+IA.mov1.name
			print juego
		elif des == 1:
			res=getElement(IA.mov2.tipo,Team.tipo)
			damage=getForm(res,IA,Team,IA.mov2.damage)
			Team.hp=Team.hp-damage
			juego = "IA uso "+IA.mov2.name
			print juego
		elif des == 2:
			res = getElement(IA.mov3.tipo,Team.tipo)
			damage=getForm(res,IA,Team,IA.mov3.damage)
			Team.hp=Team.hp-damage
			juego = "IA uso "+IA.mov3.name
			print juego
		else:
			IA.attack = IA.attack+50
			juego = "IA uso "+IA.mov4.name
			print juego

		if isNotDead(Team):
			if mov == 0:
				#resis=resistencia(Team.tipo)
				res=getElement(Team.mov1.tipo,IA.tipo)
				damage=getForm(res,Team,IA,Team.mov1.damage)
				IA.hp=IA.hp-damage
			elif mov == 1:
				res=getElement(Team.mov2.tipo,IA.tipo)
				damage=getForm(res,Team,IA,Team.mov2.damage)
				IA.hp=IA.hp-damage
			elif mov == 2:
				res=getElement(Team.mov3.tipo,IA.tipo)
				damage=getForm(res,Team,IA,Team.mov3.damage)
				IA.hp=IA.hp-damage
			else:
				res=getElement(Team.mov4.tipo,IA.tipo)
				damage=getForm(res,Team,IA,Team.mov4.damage)
				IA.hp=IA.hp-damage
		else:
			return [IA,Team,1]#1-gano IA, 2-gano player,0 continua

	else:
		if mov == 0:
			#resis=resistencia(Team.tipo)
			res=getElement(Team.mov1.tipo,IA.tipo)
			damage=getForm(res,Team,IA,Team.mov1.damage)
			IA.hp=IA.hp-damage
		elif mov == 1:
			res=getElement(Team.mov2.tipo,IA.tipo)
			damage=getForm(res,Team,IA,Team.mov2.damage)
			IA.hp=IA.hp-damage
		elif mov == 2:
			res=getElement(Team.mov3.tipo,IA.tipo)
			damage=getForm(res,Team,IA,Team.mov3.damage)
			IA.hp=IA.hp-damage
		else:
			res=getElement(Team.mov4.tipo,IA.tipo)
			damage=getForm(res,Team,IA,Team.mov4.damage)
			IA.hp=IA.hp-damage

		if isNotDead(IA):
			if des == 0:
				#resis=resistencia(Team.tipo)
				res=getElement(IA.mov1.tipo,Team.tipo)
				damage=getForm(res,IA,Team,IA.mov1.damage)
				Team.hp=Team.hp-damage
				juego = "IA uso "+IA.mov1.name
				print juego
			elif des == 1:
				res=getElement(IA.mov2.tipo,Team.tipo)
				damage=getForm(res,IA,Team,IA.mov2.damage)
				Team.hp=Team.hp-damage
				juego = "IA uso "+IA.mov2.name
				print juego
			elif des == 2:
				res=getElement(IA.mov3.tipo,Team.tipo)
				damage=getForm(res,IA,Team,IA.mov3.damage)
				Team.hp=Team.hp-damage
				juego = "IA uso "+IA.mov3.name
				print juego
			else:
				IA.attack = IA.attack+50
				juego = "IA uso "+IA.mov4.name
				print juego
		else:
			return [IA,Team,2]#1-gano IA, 2-gano player,0 continua

	return [IA,Team,0]
