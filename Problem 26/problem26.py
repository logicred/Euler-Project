#Answer = 983
#cost = 0.323s
import time

start = time.time()

limit = 1000
maxnum = 0
maxcycle = 0

def order(a,m):
    if m == 1:
        return(0)
    else:
        j = 1
        while pow(a,j) % m != 1:
            j += 1
        return(j)

def cycle(num):
    while num % 2 == 0:
        num = num // 2
    while num % 5 == 0:
        num = num // 5
    return(order(10,num))

for i in range(1, limit + 1):
    temp = cycle(i)
    if temp > maxcycle:
        maxnum = i
        maxcycle = temp
print(maxnum)

end = time.time()

print(end - start)