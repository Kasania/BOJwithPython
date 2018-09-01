#Problem Number : #5622
#-----------------------

text = input()
A = ord('A')
result = [-1]*len(text)
S = ord('S')
Z = ord('Z')
for i, s in enumerate(text):
    code = ord(s)
    if code >= S  :
        if code == Z:
            code -= 1
        code -= 1
    code -= A
    result[i] = code // 3 + 3

print(sum(result))
