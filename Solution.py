#Problem Number : #8958
#-----------------------

testCase = int(input())

for i in range(testCase):
    total = 0
    con = 0
    Str = input()
    for s in Str:
        if s == 'O':
            con += 1
            total += con
        else:
            con = 0
    print(total)