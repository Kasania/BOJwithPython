#Problem Number : #2941
#-----------------------

text = input()
cAlpha = ('c=','c-','dz=','d-','lj','nj','s=','z=')

for cA in cAlpha:
    text = text.replace(cA,'!')
print(len(text))