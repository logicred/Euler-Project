#Answer = 34029210557338
#cost = 0.004s
import time

start = time.time()

limit = 51
bino = [[0 for i in range(0, limit)] for j in range(0, limit)]
res = []
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
for i in range(0, limit):
    for j in range(0, i + 1):
        if i == j or j == 0:
            bino[i][j] = 1
        else:
            bino[i][j] = bino[i - 1][j] + bino[i - 1][j - 1]
        res += [bino[i][j]]

res = set(res)
summary = 0
for i in res:
    flag = True
    for p in prime:
        if i % (p ** 2) == 0:
            flag = False
            break
    if flag:
        summary += i
print(summary)

end = time.time()

print(end - start)