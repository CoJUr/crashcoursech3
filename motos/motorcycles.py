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
