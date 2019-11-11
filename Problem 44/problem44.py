#Answer = 5482660
#cost = 38.7s

import time
import math

start =time.time()

def pentagonal(num):
	x = (1 + math.sqrt(1 + 24 * num)) // 6
	if x * (3 * x - 1) // 2 == num:
		return True
	else:
		return False
minnum = 1000000000
flag = False
for y in range(1, 10000):
	for x in range(1, 10000):
		temp = (y + 1) * (3 * (y + 1) - 1) // 2
		s = y * (3 * y - 1) // 2
		t = x * (3 * x - 1) // 2
		if y > x and pentagonal(s - t) and pentagonal(s + t) and s - t < minnum:
			minnum = s - t
		if y - x == 1 and temp - 1 > minnum:
			#print(minnum, x, y)
			flag = True
	if flag == True:
		break

print(minnum)
end = time.time()

print(end -start)