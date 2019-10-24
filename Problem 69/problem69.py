#Answer = 510510
#cost < 0.001s

import time
import math

start = time.time()

def is_prime(num):
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

pro = 1
for x in range(2, 100):
	if is_prime(x):
		if pro * x <= 1000000:
			pro *= x
		else:
			break
print(pro)

end = time.time()

print(end - start)