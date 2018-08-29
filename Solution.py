#Problem Number : #1463
#-----------------------

X = int(input())

resultArray = [9999]*(X+2)
resultArray[1] = 0
for i in range(1,X+1):
    if i*3 <= X:
        if resultArray[i * 3] > resultArray[i]+1:
            resultArray[i * 3] = resultArray[i]+1
    if i*2 <= X:
        if resultArray[i * 2] > resultArray[i]+1:
            resultArray[i * 2] = resultArray[i]+1
    if resultArray[i + 1] > resultArray[i]+1:
        resultArray[i + 1] = resultArray[i]+1
print(resultArray[X])
