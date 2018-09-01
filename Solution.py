#Problem Number : #1316
#-----------------------

case = int(input())

total = 0
a = ord('a')
for i in range(case):
    text = input()
    prv = ''
    isChecked = [False]*27

    for s in text:

        if prv != s:
            sCode = ord(s)-a
            if isChecked[sCode]:
                total -= 1
                break
            else:
                isChecked[sCode] = True
                prv = s
    total += 1

print(total)