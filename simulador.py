from decision import *
from conclusion import *
from batalla import *
from getStrategy import *
import os

def desProfit(strategy, profit, buff):
	if profit[0]==0:
		profit[0]=profit[1]
	if profit[1]<profit[0] and len(strategy.mix)>0:
		strategy.tryAnother = True
		if len(strategy.util)>1:
			del strategy.util[1]
		profit[1]=0
	elif profit[0]<profit[1] and len(strategy.mix)>0:
		if profit[1]>0:
			strategy.tryAnother = False
		else:
			strategy.tryAnother = True
		if len(strategy.util)>1:
			strategy.util[0] = strategy.util[1]
		profit[0] = profit[1]
		profit[1] = 0
	elif profit[0]==profit[1] and len(strategy.mix)>0:
		if profit[0]<0:
			strategy.tryAnother = True
			profit[1] = 0
		else:
			strategy.tryAnother = False
			if len(strategy.util)>1:
				del strategy.util[0]
			profit[1] =0
	else:
		if profit[1]<profit[0]:
			strategy.tryAnother = False
			if len(strategy.util)>1:
				del strategy.util[1]
			profit[1]=0
		elif profit[0]<profit[1]:
			if len(strategy.util)>1:
				strategy.util[0] = strategy.util[1]
			profit[0] = profit[1]
			profit[1] = 0
			strategy.tryAnother = False
		else:
			strategy.tryAnother = False

def nesDecision(profit, strategy):
	if not(profit[1]==0 and profit[0]==0):
		if profit[0] == 0:
			profit[0] = profit[1]
		if profit[0]<10.0 and len(strategy.mix) >0:
			strategy.newone = 1
		else:
			strategy.newone = 0
	else:
		strategy.newone = 0


def simulacion(IA,Team, strategy):
	a=True
	ter = 0
	profit =[0,0]
	buff = 0

	while a:
		mov=decision(Team,IA)
		mov=mov-1
		os.system('clear')
		des = getStrategy(Team.tipo, strategy[Team.tipo], profit)	
		res=batalla(mov,IA,Team, des)
		profit[1] =profit[1] + float((res[3][0])-(res[3][1]))
		nesDecision(profit, strategy[Team.tipo])
		if res[3][0] == 0:
			buff = buff+1
		if strategy[Team.tipo].newone==1:
			desProfit(strategy[Team.tipo], profit, buff)
		else:
			profit[1]=0
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

	