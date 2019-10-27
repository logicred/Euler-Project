#Answer = 127035954683
#cost = 9.65s

import time

start = time.time()

maxnum = 10000 + 1
test = [0 for y in range(0, maxnum)]

for x in range(1, maxnum):
    y = x ** 3
    test[x]=''.join(sorted(str(y)))

for x in range(1, maxnum - 1):
    num = 1
    for y in range(x + 1, maxnum):
        if test[x] == test[y]:
            num += 1
    if num == 5:
        print(x ** 3)
        break

end = time.time()

print(end - start)