#Problem Number : #1110
#-----------------------

N = int(input())
V = N
cnt = 0

while True :
    if V < 10:
        V *= 11
    else:
        V = (V%10*10) + ((V//10 + V%10)%10)
    cnt +=1
    if V == N:
        break
print (cnt)