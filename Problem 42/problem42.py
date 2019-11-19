#Answer = 162
#cost = 0.007s
import time

start = time.time()

triangle = [n * (n +  1) // 2 for n in range(1, 40)]

def tri_word(s):
    global triangle
    summary = 0
    for i in s:
        if i == '"':
            continue
        summary += (ord(i) - ord('A') + 1)
    if summary in triangle:
        return True
    else:
        return False

fi = open(r'p042_words.txt','r')
f = fi.read()
L = []
y = 0
summary = 0
for x in range(0, len(f)):
    if f[x] == ',':
        L += [str(f[y:x])]
        y = x + 1
L += [str(f[y:])]
for x in L:
    if tri_word(x):
        summary += 1
print(summary)

end = time.time()

print(end - start)