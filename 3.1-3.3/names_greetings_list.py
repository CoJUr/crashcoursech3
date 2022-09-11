names = ["ben", "jerry", "cellulite"]

print(names[2])
print(names[0])
print(names[1])

print("My favorite friend is you, " + names[0].title() + ".")
print(f"My favorite friend is you, {names[1].title()}.")
print("My LEAST favorite friend is you, {}.".format(names[2].title()))

my_list = ['cruise', 'plane', 'car', 'train', 'boat']

print("Some day I'd like to go on a " + my_list[0])
print(f"It's been a while since I've been on a {my_list[1]}")
print("I'd like to drive a nicer {}.".format(my_list[2]))
print("I'd like to take a trip on a fast {}.".format(my_list[3]))