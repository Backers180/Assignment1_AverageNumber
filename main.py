entries = 0     # These are the varibales for the program
total = 0     
numbers = []
gate = 0

print("How many numbers would you like to find the average of?")
entries = int(input())                                            

print("please enter your numbers, one at a time:")

while gate < entries:
  numbers.append(int(input()))
  gate += 1

for entry in numbers:
  total += entry

print("The average of your numbers is:", total / entries)

