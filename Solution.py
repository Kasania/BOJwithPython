#Problem Number : #4344
#-----------------------

testCase = int(input())

for i in range(testCase):
    value = list(map(int,input().split()))
    numOfPerson = value[0]
    scores = value[1:]
    avg = sum(scores)/numOfPerson
    highRank = 0
    for score in scores:
        if score > avg:
            highRank += 1
    print('%.3f%%' % round((highRank/numOfPerson)*100,3))
