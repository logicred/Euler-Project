#Answer = 871198282
#cost = 0.0289s

import time

start = time.time()

def name_score(s):
    score = 0
    for x in s:
        if x == '"':
            continue
        score += (ord(x) - 64)
    return score


try:
    fi = open(r'p022_names.txt','r')
    f = fi.read()
finally:
    if fi:
        fi.close()

L = []
y = 0

for x in range(0, len(f)):
    if f[x] == ',':
        #print(f[y:x], num)
        #score += name_score(f[y:x]) * num
        L += [str(f[y:x])]
        y = x + 1
L += [str(f[y:])]

L = sorted(L)
score = 0
num = 1
for x in L:
    score += num * name_score(x)
    num += 1

print(score)

end = time.time()

print(end - start)