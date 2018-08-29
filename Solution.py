#Problem Number : #10039
#-----------------------

scores = [0]*5

num = 0
for i in scores:
    s = int(input())
    if s < 40:
        s = 40
    scores[num] = s
    num += 1
print(int(sum(scores)/5))
