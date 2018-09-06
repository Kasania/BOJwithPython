#Problem Number : #10250
#-----------------------

testCase = int(input())

for T in range(testCase):
    H,W,N = map(int,input().split())

    Y = 0
    X = 1
    cnt = 0
    while True:
        if Y > H :
            Y = 1
            X += 1
        if cnt == N:
            break
        Y += 1
        cnt += 1
    print( Y*100 + X)
