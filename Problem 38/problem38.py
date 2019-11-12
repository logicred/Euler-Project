#Answer = 932718654
#cost = 0.0638s

import time

start = time.time()

def pan_mul(num):
	s = ''
	for y in range(1, 10):
		s = s + str(num * y)
		if len(s) < 9:
			continue
		elif len(s) > 9:
			return False, '0'
		else:
			t = set([str(x) for x in range(1, 10)])
			if t == set(s):
				return True, s
			else:
				return False, '0'
	return False, '0'
maxnum = 0
for x in range(1, 9999 + 1):
	a, b = pan_mul(x)
	if a and maxnum < int(b):
		maxnum = int(b)
print(maxnum)

end = time.time()

print(end - start)