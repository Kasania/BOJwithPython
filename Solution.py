#Solution Number : #11721
#-----------------------

quotation = input()
n = 0
length = len(quotation)
rep = length // 10
while n < rep:
    print(quotation[n*10:(n+1)*10])
    n += 1
print(quotation[n*10:])