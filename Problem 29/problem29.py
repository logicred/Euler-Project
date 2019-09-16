#Answer = 9183
#cost = 0.0110s


import time

start = time.time()

s = set([pow(a,b) for a in range(2, 100 + 1) for b in range(2, 100 + 1)])
print(len(s))

end = time.time()

print(end - start)