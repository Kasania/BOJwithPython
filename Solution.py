#Problem Number : #1157
#-----------------------
text = input().upper()

result = [0]*27
A = ord('A')
Z = ord('Z')
for i in text:
    result[ord(i)-A] += 1

maxN = max(result)
if result.count(maxN) > 1:
    print('?')
else:
    print(chr(A + result.index(maxN)))