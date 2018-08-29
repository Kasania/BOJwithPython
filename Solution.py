#Problem Number : #2577
#-----------------------

mul = str(int(input())*int(input())*int(input()))
for i in range(10):
    print(mul.count(str(i)))
