#Problem Number : #1193
#-----------------------

inputNumber = int(input())
sumNum = 1
tNum = 0

while inputNumber > tNum:
    tNum += sumNum
    sumNum += 1

M = 0
S = 0
if sumNum % 2 == 0:
    S = tNum - inputNumber + 1
    M = sumNum - S
else:
    M = tNum - inputNumber + 1
    S = sumNum - M
print('%d/%d'%(S,M))
