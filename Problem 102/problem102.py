#Answer = 228
#cost = 0.022s
import time

start = time.time()

f = open('p102_triangles.txt','r')
summary = 0

def area(L):
    x1 = L[0]
    y1 = L[1]
    x2 = L[2]
    y2 = L[3]
    x3 = L[4]
    y3 = L[5]
    return(abs(x1 * (y2 - y3) - x2 * (y1 - y3) + x3 * (y1 - y2)))

def contain_zero(L):
    temp = [0, 0, L[2], L[3], L[4], L[5]]
    sum1 = area(temp)
    temp = [L[0], L[1], 0, 0, L[4], L[5]]
    sum2 = area(temp)
    temp = [L[0], L[1], L[2], L[3], 0, 0]
    sum3 = area(temp)
    return ((sum1 + sum2 + sum3) == area(L))

try:
    while True:
        L = []
        fi = f.readline()
        if fi:
            i = j = 0
            while True:
                if fi[i] == ',':
                    L += [int(fi[j:i])]
                    j = i + 1
                if i == len(fi) - 1:
                    L += [int(fi[j:i + 1])]
                    break
                i += 1
            if contain_zero(L):
                summary += 1
        else:
            break
finally:
    f.close()

print(summary)

end = time.time()

print(end - start)