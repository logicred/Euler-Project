#Answer = 8739992577
#cost = 0.454s

import time

start = time.time()

r = 1
n = 10000000000
for x in range(0 ,978807):
    r = (r * 256) % n
r = (r * 28433 * 2 + 1) % n
print(r)

end = time.time()

print(end - start)