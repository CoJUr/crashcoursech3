answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# utilizing keywords and and or to check multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# improve readability by using parentheses around each condition
print((age_0 >= 21) and (age_1 >= 21))

# using or to check multiple conditions - either or both conditions must be true
age_0 = 22
age_1 = 18
print((age_0 >= 21) or (age_1 >= 21))

# keyword in to check if a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)