#Answer = 0.5731441
#cost = 0.132s
import time

start = time.time()

L1 = [1, 2, 3, 4]
L2 = [1, 2, 3, 4, 5, 6]

def dice_game(L, num):
    t1 = []
    for i in L:
        t1 += [i]
    for k in range(0, num): 
        t2 = []
        for i in t1:
            for j in L:
                t2 += [i + j]
        t1 = t2
    return t1

Peter = dice_game(L1, 8)
plist = [0 for i in range(9, 36 + 1)]
Colin = dice_game(L2, 5)
clist = [0 for i in range(6, 216 + 1)]
for i in Peter:
    plist[i - 9] += 1
for i in Colin:
    clist[i - 6] += 1
win = 0
lose = 0
whole = 0
for i in range(0, len(plist)):
    for j in range(0, len(clist)):
        if i + 9 > j + 6:
            win += plist[i] * clist[j]
        whole += plist[i] * clist[j]
print(win/whole)

end = time.time()

print(end - start)