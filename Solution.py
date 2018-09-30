#Problem Number : #2231
#-----------------------

def DigitSum (x):
    strx = str(x)
    sumx = x
    for s in strx:
        sumx = sumx + int(s)
    return sumx
#--------------------------
N = int(input())
generator = 0
for i in range(N - ( len( str(N) ) * 9 ), N):
    if DigitSum(i) == N:
        generator = i
        break
print(generator)