#Problem Number : #2920
#-----------------------

X = input().split()
rX = list(reversed(X))

asc = True
des = True
mix = False

for i in range(1,9):
    if i != int(X[i-1]):
        asc = False
    if i != int(rX[i-1]):
        des = False
if asc:
    print('ascending')
elif des:
    print('descending')
else:
    print('mixed')
