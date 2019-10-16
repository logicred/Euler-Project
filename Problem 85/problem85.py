#Answer = 2772
#cost = 0.029s
import time

start = time.time()

minnum = limit = 2000000
num = 2000
x, y = 0, 0

def rectangle(x, y):
    return (x * (x + 1) * y * (y + 1)) // 4

for i in range(1, num):
    upp = i
    low = 1
    mid = (upp + low) // 2
    t1 = rectangle(i, upp)
    t2 = rectangle(i, mid)
    t3 = rectangle(i, low)
    while mid != upp and mid != low:
        if t2 > limit:
            upp = mid
            t1 = t2
        else:
            low = mid
            t3 = t2
        mid = (upp + low) // 2
        t2 = rectangle(i, mid)
    if abs(t3 - limit) > abs(t1 - limit):
        temp = abs(t1 - limit)
        tx, ty = i, upp
    else:
        temp = abs(t3 - limit)
        tx, ty = i, low
    if temp < minnum:
        minnum = temp
        x, y = tx, ty
print(x * y, limit - minnum)

end = time.time()

print(end - start)