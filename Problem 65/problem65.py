#Answer = 272
#cost < 0.001s
import time

start = time.time()

limit = 100
con_frac = [0 for i in range(0, limit)]
summary = 0
for i in range(0, limit):
    if i == 0:
        con_frac[i] = 2
    elif i % 3 == 2:
        con_frac[i] = 2 * (i // 3 + 1)
    else:
        con_frac[i] = 1

def e_frac(num):
    global con_frac
    numer = 1
    diver = con_frac[num - 1]
    for i in range(num - 1, 0, -1):
        numer, diver = diver, (numer + diver * con_frac[i - 1])
    return diver
s = str(e_frac(100))
for i in s:
    summary += int(i)
print(summary)

end = time.time()

print(end - start)