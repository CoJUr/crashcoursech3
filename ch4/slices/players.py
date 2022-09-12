# to work with a slice, specify the first and last idx to work with. e.g. indices 0-3 to work with 0,1,2
players = ['charles', 'martine', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

# omit first idx to start at the beginning of the list or 2nd idx to go to until the end of the list
print(players[:3])

print(players[2:])

# can use a 3rd idx to specify a step size
print(players[-4::3])

# loop through a subset of a list
players = ['charles', 'martine', 'michael', 'florence', 'eli']
print("the first three players on my team are: ")
for player in players[:3]:
    print(player.title())


