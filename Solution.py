#Problem Number : #1011
#-----------------------

import math

testCase = int(input())

for T in range(testCase):
    pos = list(map(int,input().split()))
    gap = pos[1] - pos[0]
    i = 1
    # 1+2+3+...+ n +...+3+2+1 = n^2
    while i*i <= gap:
        i += 1
    i -= 1

    # n^2에 속하지 못한 부분의 길이
    gap = math.ceil( (gap-i*i) / i)
    print(i*2 - 1 + gap)
