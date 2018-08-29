#Problem Number : #1065
#-----------------------

X = int(input())
result = 99
if X<100:
    print(X)
else:
    for i in range(100,X+1):
        S = str(i)
        S1 = int(S[0])
        S2 = int(S[1])
        S3 = int(S[2])
        D1 = S1 - S2
        D2 = S2 - S3
        if D1 == D2:
            result +=1
    print(result)
