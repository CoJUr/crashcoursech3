squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# can omit temp variable and append each value directly
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# finding min, max, and sum of lists
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehensions: allow generation of lists with one line of code, can auto append as well
squares = [value**2 for value in range(1,11)]
print(squares)
