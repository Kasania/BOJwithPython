#Problem Number : #1546
#-----------------------

numOfSubject = int(input())
scoresOfSubject = sorted(map(int,input().split()))
avg = (sum(scoresOfSubject) / numOfSubject) / scoresOfSubject[-1] * 100
print(avg)
