#Answer = 31875000
#cost = 0.222s

import time

start = time.time()

limit = 1000
for c in range(1, limit // 2):
    for a in range(1, (limit - c) // 2):
        if a ** 2 + (limit - a - c) ** 2 == c ** 2:
            print(a * (limit - a - c) * c)
            break

end = time.time()

print(end - start)