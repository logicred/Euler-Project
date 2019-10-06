#Answer = 906609 993 913
#cost = 0.291

import time

start = time.time()

def palindrome(a, b):
    #print(1)
    summary = a * b
    num = str(summary)
    i = 0
    j = len(num) - 1
    while i < j:
        if num[i] != num[j]:
            return False
        i += 1
        j -= 1
    return True

maxnum = 0
m1 = 0
m2 = 0
for i in range(999, 99, -1):
    #print(0)
    j = i
    while j >= 100:
        temp = i * j
        if temp % 11 == 0 and palindrome(i, j) == True and temp > maxnum:
            maxnum = temp
            m1 = i
            m2 = j
        j -= 1

print(maxnum, m1, m2)

end = time.time()

print(end - start)