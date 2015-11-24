def decision(team,IA):
	print "***********************************"
	cadena = "Team: "+str(team.hp)+"     "+"IA: "+str(IA.hp)
	print cadena
	cadena1 = team.mov1.name + "----------- 1"
	cadena2 = team.mov2.name + "----------- 2"
	cadena3 = team.mov3.name + "----------- 3"
	cadena4 = team.mov4.name + "----------- 4"
	print cadena1
	print cadena2
	print cadena3
	print cadena4
	c = int(raw_input("Decision:"))
	return c