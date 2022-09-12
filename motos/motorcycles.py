motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# insert method can add an element at any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, "yamborghini")
print(motorcycles)

# del statement removes an item from a list. assumes known index
del motorcycles[1]
print(motorcycles)

# pop method removes the last item in a list, but lets you work with it, e.g. turning an active user to an inactive user
popped_bike = motorcycles.pop()
print(motorcycles)
print(popped_bike)

print(f"The last bike I had was a {popped_bike.title()}.")

# include the index of the item in the pop method to remove a specific item
first_owned = motorcycles.pop(0)
print(f"My 1st motorbike was a {first_owned.title()}.")

# if only know the value and not position of the item you want to remove, use remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)
# or use remove to work with the item you're removing.
# note: only removes the first occurrence of the value. will need to use a loop if possibility of multiple occurrences
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} \nis too expensive for me right now")


ingredients_list = ['butter', 'whole milk', 'sugar', 'flour', 'eggs', 'baking powder', 'frosting']

print("SortED ingredients: ")
print(sorted(ingredients_list))
print(ingredients_list)

print("Reversed (temp) sortED ingredients: ")
print(sorted(ingredients_list, reverse=True))

print(ingredients_list)
print("Reversed (the permanent way): ")
print(ingredients_list.reverse())
print(ingredients_list)

# print("""Reversed (the permanent way) again: {}
# """.format(ingredients_list.reverse()))

ingredients_list.reverse()
print("Post double reverse: " + str(ingredients_list))

ingredients_list.sort()
print("Permanently sorted: " + str(ingredients_list))

ingredients_list.sort(reverse=True)
print("Permanently reverse sorted: " + str(ingredients_list))

print("length of the ingredients list = " + str(len(ingredients_list)))

fattening = 'butter'
ingredients_list.remove(fattening)
print(f"I had to remove the dangerous ingredient {fattening}. now the list is only: {ingredients_list}")

last_item = ingredients_list.pop()
print(f"the last item was {last_item}. now the list is only: {ingredients_list}")

del ingredients_list[1]
print("deleted the item at position 1; sugar. left with : " + str(ingredients_list))

ingredients_list.insert(1, 'sugar')
print("Couldn't live without it, so I put sugar back in")
print(ingredients_list)

ingredients_list.append('pie crust')
print("I forgot the pie crust! added it in.")
print(ingredients_list)

ingredients_list[1] = 'swerve'
print("I'm trying to be healthy, so I'm replacing sugar with swerve.")
print(ingredients_list)

almost_last = ingredients_list[-2]
print(f"the item before the last item is {almost_last}")

# index error
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])

print(motorcycles[-1])