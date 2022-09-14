fav_pizzas = ['meat lovers', 'pepperoni', 'hawaiian']

for pizza in fav_pizzas:
    print("One of my favorite pizzas is " + pizza)

print("""
I believe I might
write a program about how
great pizza is imo.""")
print("I really love pizza!")

we_are_similar = ['dolphin', 'human', 'chimpanzee']

for animal in we_are_similar:
    print(animal)
    print("The " + animal + " is like the others, in part, because it is a mammal.")

print("All of these animals are mammals and highly intelligent.")



friend_pizzas = fav_pizzas[:]
print(friend_pizzas)
fav_pizzas.append('smokehouse')
friend_pizzas.append('vegetarian')
print(friend_pizzas, fav_pizzas)

print("My favorite pizzas are:")
for mine in fav_pizzas:
    print(mine)

print("My friend's favorite pizzas are:")
for theirs in friend_pizzas:
    print(theirs)
