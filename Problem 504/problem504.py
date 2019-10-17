#Answer = 694687
#cost = 161.3s
import time
import math

start = time.time()

limit = 100 + 1
gcdmap = [[math.gcd(i, j) for i in range(0, limit)] for j in range(0, limit)]
summary = 0

for a in range(1, limit):
    for b in range(1, limit):
        for c in range(1, limit):
            for d in range(1, limit):
                area = (a + c) * (b + d)
                line = gcdmap[a][b] + gcdmap[b][c] + gcdmap[c][d] + gcdmap[d][a]
                inside = (area - line) // 2 + 1
                
                if math.sqrt(inside) == int(math.sqrt(inside)):
                    summary += 1

print(summary)

end = time.time()

print(end - start)