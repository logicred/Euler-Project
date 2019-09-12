import time

start = time.time()

def createlist(num):
	L = [0] * num
	for x in range(2, num):
		if not L[x] and x + 1 < num:
			y = 2 * x
			while y < num:
				L[y] += 1
				y += x
	return L

pr = createlist(200000)
x = 210
while x >= 210 and x < 200000:
	if pr[x] == 4 and pr[x - 1] == 4 and pr[x - 2] == 4 and pr[x - 3] == 4:
		print(x, x - 1, x - 2, x - 3)
		break
	x += 1

end = time.time()

print(end - start)
