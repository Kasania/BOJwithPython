#Problem Number : #2775
#-----------------------

apt = [[0 for x in range(15)] for y in range(15)]
for i in range(1,15):
    apt[0][i] = i

for y in range(1,15):
    for x in range(1,15):
        if x == 1:
            apt[y][x] = apt[y-1][x]
        else:
            cnt = 0
            for k in range (1,x+1):
                cnt += apt[y-1][k]
            apt[y][x] = cnt

for T in range(int(input())):
    k = int(input())
    n = int(input())
    print(apt[k][n])
