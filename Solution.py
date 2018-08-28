#Problem Number : #4673
#-----------------------

def d(i):
    target = str(i)
    result = i
    for n in range(len(target)):
        result += int(target[n])
    return result

dArray = [None]*10001

for j in range(1,10001):
    if d(j)<=10000:
        dArray[d(j)] = j

for j in range(1,10001):
    if not(dArray[j]):
        print(j)
        