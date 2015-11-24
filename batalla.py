import random
#Damage=(attack+damage-defense)resistance

def isNotDead(per):
	if per.hp>0:
		return True
	return False

def batalla(mov,IA,Team):
	des=random.randint(0,3)
	if IA.speed>Team.speed:
		if mov == 0:
			#resis=resistencia(Team.tipo)
			damage=(IA.mov1.damage+IA.attack-Team.defense)
			Team.hp=Team.hp-damage
		elif mov == 1:
			damage=(IA.mov2.damage+IA.attack-Team.defense)
			Team.hp=Team.hp-damage
		elif mov == 2:
			damage=(IA.mov3.damage+IA.attack-Team.defense)
			Team.hp=Team.hp-damage
		else:
			IA.attack = IA.attack+50

		if isNotDead(Team):
			if mov == 0:
				#resis=resistencia(Team.tipo)
				damage=(Team.mov1.damage+Team.attack-IA.defense)
				IA.hp=IA.hp-damage
			elif mov == 1:
				damage=(Team.mov2.damage+Team.attack-IA.defense)
				IA.hp=IA.hp-damage
			elif mov == 2:
				damage=(Team.mov3.damage+Team.attack-IA.defense)
				IA.hp=IA.hp-damage
			else:
				damage=(Team.mov4.damage+Team.attack-IA.defense)
				IA.hp=IA.hp-damage
		else:
			return [IA,Team,1]#1-gano IA, 2-gano player,0 continua

	else:
		if mov == 0:
			#resis=resistencia(Team.tipo)
			damage=(Team.mov1.damage+Team.attack-IA.defense)
			IA.hp=IA.hp-damage
		elif mov == 1:
			damage=(Team.mov2.damage+Team.attack-IA.defense)
			IA.hp=IA.hp-damage
		elif mov == 2:
			damage=(Team.mov3.damage+Team.attack-IA.defense)
			IA.hp=IA.hp-damage
		else:
			damage=(Team.mov4.damage+Team.attack-IA.defense)
			IA.hp=IA.hp-damage

		if isNotDead(IA):
			if mov == 0:
				#resis=resistencia(Team.tipo)
				damage=(IA.mov1.damage+IA.attack-Team.defense)
				Team.hp=Team.hp-damage
			elif mov == 1:
				damage=(IA.mov2.damage+IA.attack-Team.defense)
				Team.hp=Team.hp-damage
			elif mov == 2:
				damage=(IA.mov3.damage+IA.attack-Team.defense)
				Team.hp=Team.hp-damage
			else:
				IA.attack = IA.attack+50
		else:
			return [IA,Team,2]#1-gano IA, 2-gano player,0 continua

	return [IA,Team,0]
