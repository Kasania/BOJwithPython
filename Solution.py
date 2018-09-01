#Problem Number : #2908
#-----------------------

numbers = input().split()
numbers[0] = int(numbers[0][::-1])
numbers[1] = int(numbers[1][::-1])

print(numbers[0] if numbers[0] > numbers[1] else numbers[1])
