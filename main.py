entries = 0
numbers = []
total = 0

print("Please enter the numbers you want the average of: ")
print("When you finish entering your numbers, input 'end'")
while True:
  value = input()
  if value == "end":
      for entry in numbers:
        total += entry
      print("The average of your numbers is:", total / entries)
  else:
    entries += 1
    numbers.append(int(value))