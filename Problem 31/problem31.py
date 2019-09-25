#Answer = 73682
#cost = 0.0499s

import time

start = time.time()

limit = 200
coin = [200, 100, 50, 20, 10, 5, 2, 1]
def find_coin(coin, x, y):
    summary = 0
    if y == 7 or x == 0:
        summary = 1
    else:
        i = 0
        while i * coin[y] <= x:
            summary += find_coin(coin, x - i * coin[y], y + 1)
            i += 1
    return summary
summary = find_coin(coin, limit, 0)
print(summary)

end = time.time()

print(end - start)