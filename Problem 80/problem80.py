#Answer = 40886
#cost = 0.176s

import time

start = time.time()

limit = 100
pr = 100
summary = 0

def root_dig(x):
    global pr
    temp = x ** (1/2)
    res = 0
    if temp == int(temp):
        return res
    else:
        a = pow(10, 100)
        eq = x * a ** 2
        upp = (int(temp) + 1) * a
        low = int(temp) * a
        mid = (upp + low) // 2
        while mid != upp and mid != low:
            upp_loss = abs(upp ** 2 - eq)
            low_loss = abs(low ** 2 - eq)
            mid_loss = abs(mid ** 2 - eq)
            if upp_loss > low_loss:
                upp = mid
            else:
                low = mid
            mid = (upp + low) // 2
        if upp ** 2 > eq:
            right = low
        else:
            right = upp
        s = str(right)
        for i in s[:pr]:
            res += int(i)
        return res

for i in range(2, limit + 1):
    summary += root_dig(i)

print(summary)

end = time.time()

print(end - start)