#Problem Number : #10871
#-----------------------

condition = list(map(int,input().split()))
numbers = list(map(int,input().split()))

i = 0
nList = list()
length = len(numbers)
while i < length:
    if numbers[i] < condition[1]:
        nList.append(numbers[i])
    i += 1
print(' '.join(map(str,nList)))
