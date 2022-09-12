up_to_twenty = [value for value in range(1, 21)]
print(up_to_twenty)

loop_20 = []
for i in range(1, 21):
    loop_20.append(i)
print(loop_20)

# one_million = [value for value in range(1, 1000001)]
a_milli = []
for value in range(1, 1000001):
    a_milli.append(value)
    # print(value)

print("Should be 1: " + str(min(a_milli)))
print("Should be 1mil: " + str(max(a_milli)))

summed_milli = sum(a_milli)
print(summed_milli)

odds_only = []
for odd in range(1, 20, 2):
    odds_only.append(odd)
    print(odd)
print(odds_only)

odds = [odd for odd in range(1, 20, 2)]
print(odds)

multis_of_3 = []
for multi in range(3, 31, 3):
    multis_of_3.append(multi)
    print(multi)

# list the first 10 cubes and print eah value in a for loop
ten_cubes = []
for cube in range(1, 11):
    ten_cubes.append(cube**3)
    print(cube**3)
print(ten_cubes)

ten_comp_cubes = [cube ** 3 for cube in range(1, 11)]
print(ten_comp_cubes)

