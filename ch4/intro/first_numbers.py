# range() function to generate a series of numbers
for value in range(1, 5):
    print(value)

# pass it only 1 argument to get a range starting at 0
for value in range(6):
    print(value)

print("####################")
# wrap a call to range() in a list() function to make a list of numbers
numbers = list(range(1, 5))
print(numbers)

even_numbers = list(range(2, 11, 2))
# 3rd argument is the step size
print(even_numbers)




