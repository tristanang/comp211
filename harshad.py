def addition(x):
	if x == 0:
		return 0
	else:
		return x%10 + addition(x//10)

def harshad(n):
	L = []
	count = 1
	while len(L) < n:
		if count%addition(count)==0:
			L.append(count)
		count = count + 1
	return L[n-1]
