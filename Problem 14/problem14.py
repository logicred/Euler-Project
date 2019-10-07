#Answer = 837799 525
#cost = 48.2s

import time

start = time.time()

limit = 1000000
longest = terms = 0
for i in range(1, limit + 1):
    if (i % 2 == 1 and i <= limit // 2) or ((i - 1) % 3 == 0 and (((i - 1) // 3) % 2 == 1)):
        continue
    j = i
    this_terms = 1
    while j != 1:
        this_terms += 1
        if this_terms > terms:
            terms = this_terms
            longest = i
        if j % 2 == 0:
            j /= 2
        else:
            j = 3 * j + 1
print(longest, terms)
end = time.time()

print(end - start)