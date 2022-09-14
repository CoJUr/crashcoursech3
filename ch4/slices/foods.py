my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
print("My favorite foods: " + str(my_foods))

print("Friends favorites = " + str(friends_foods))


# the lists are separate, so modifying one doesn't affect the other
my_foods.append('cannoli')
friends_foods.append('catsup')
print("My favorite foods: " + str(my_foods))
print("Friends favorites = " + str(friends_foods))

# copying without slices
# friends_foods = my_foods
# the lists are now the same, so modifying one affects the other
my_foods.append('cheese')
print(friends_foods, my_foods)

for food in my_foods:
    print(food + " is one of my favorite foods.")

for food in friends_foods:
    print(food + " is one of my FRIEND's favorite foods.")

