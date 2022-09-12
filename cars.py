cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
print(cars)

# reverse sort order (perm) achieved with reverse=True passed to the sort() method
cars.sort(reverse=True)
print(cars)

# sort() method is permanent, but sortED() function is temporary
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list: " + str(cars))
print("\nHeres the sorted list : " + str(sorted(cars)))
print("After sortED() we're back to this: " + str(cars))

# reverse() method reverses the original order (perm), but doesn't sort
cars.reverse()
print(cars)

# applying reverse() a second time returns the list to its original order
cars.reverse()
print(cars)

# use len() function to find length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

desired_destinations = ['Ireland', 'Australia', 'Costa Rica', 'Japan', 'Antarctica']
print("My bucket list: " + str(desired_destinations))

print(sorted(desired_destinations))
print("Post-sortED: \n" + str(desired_destinations))
print("Temp reverse sort inc: " + str(sorted(desired_destinations, reverse=True)))
print("back to normal")
print(desired_destinations)
print("####################")

print("Using reverse() method - permanent!")
desired_destinations.reverse()
print(desired_destinations)

print("reversing the reverse with reverse() method")
desired_destinations.reverse()
print(desired_destinations)

desired_destinations.sort()
print("Sorted list: - permanent sort")
print(desired_destinations)

desired_destinations.sort(reverse=True)
print("Finally sorted (permanently) in reverse with sort(reverse=True)")
print(desired_destinations)
