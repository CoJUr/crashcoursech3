dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

my_t = (3,)
print(my_t)
print(dimensions)

# looping through tuples works the same as lists
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

# can't modify a tuple, but can assign a new value to a variable representing a tuple
dimensions = (400, 100)
print("\nModified dimensions... ")
for dimension in dimensions:
    print(dimension)

