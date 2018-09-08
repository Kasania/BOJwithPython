#Problem Number : #1149
#-----------------------

CurValue = [0]*3
PreValue = [0]*3

for t in range(int(input())):
    CurValue = list(map(int,input().split()))
    CurValue[0] += min(PreValue[1], PreValue[2])
    CurValue[1] += min(PreValue[0], PreValue[2])
    CurValue[2] += min(PreValue[0], PreValue[1])
    PreValue = CurValue[:]

print(min(PreValue))