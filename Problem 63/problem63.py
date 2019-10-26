#Answer = 49
#cost < 0.001s

import time

start = time.time()

n = 0
for x in range(1, 100):
	s = pow(10, (x - 1) / x)
	if s >= 10:
		break
	else:
		n = n + int(10 - s)
print(n)

end = time.time()

print(end - start)