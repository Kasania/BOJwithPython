#Problem Number : #2675
#-----------------------

case = int(input())
for j in range(case):
    S = input().split()
    R = int(S.pop(0))
    T = ''
    for s in S[0]:
        for i in range(R):
            T += s
    print(T)

