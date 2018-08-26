#Problem Number : #15552
#-----------------------

import sys

case = int(sys.stdin.readline().rstrip())
quote = ''
i = 0
while i< case:
    quote = sys.stdin.readline().rstrip().split(' ')
    print(int(quote[0])+int(quote[1]))
    i += 1
