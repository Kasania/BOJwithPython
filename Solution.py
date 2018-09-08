#Problem Number : #1475
#-----------------------

import sys
import math

number = list(sys.stdin.readline())[:-1]
cnt = [0]*10

for i in number:
    cnt[int(i)] += 1
cnt[6] = math.ceil((cnt[6] + cnt[9])/2)
cnt[9] = cnt[6]

print(max(cnt))
