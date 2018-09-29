#Problem Number : #2490
#-----------------------

token = ('D','C','B','A','E')
for x in range(3):
    numbers = sum(map(int,input().split()))
    print(token[numbers])
