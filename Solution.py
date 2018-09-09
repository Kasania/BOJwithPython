#Problem Number : #1978
#-----------------------

N = int(input())
numbers = list(map(int,input().split()))

primeNumbers = [True]*1001
primeNumbers[1] = False
cnt = 0

for i in range(2,1001):
    x = i
    while True:
        x += i
        if x>1000:
            break
        primeNumbers[x] = False

for V in numbers:
    if primeNumbers[V]:
        cnt += 1

print(cnt)