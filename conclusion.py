

def conclusion(res):
	if res[2] == 1:
		return 1
	elif res[2] == 2:
		return 2
	else:
		if res[0].hp>0:
			if res[1].hp>0:
				return 0
			return 1
		return 2