#Problem Number : #2292
#-----------------------

dst = int(input())
if dst == 1:
    print('1')
else:
    dst -= 1
    currentRoom = 1
    while True:
        if currentRoom * 6 >= dst:
            break
        else:
            dst -= currentRoom*6
            currentRoom += 1
    print(currentRoom+1)
