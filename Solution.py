#Problem Number : #10250
#-----------------------

testCase = int(input())

for T in range(testCase):
    H,W,N = map(int,input().split())
    Y = N % H
    if Y == 0:
        Y = H
    X = (N - 1) // H + 1
    print( Y*100 + X)