current_users = ['benji', 'ahsam19', 'killakam', 'engy', 'Lamp']
current_users_lower = [user.lower() for user in current_users]

new_users = ['Benji', 'jacko2', 'bak2bak', '2chainz', 'LAMP']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is taken. Please pick a different username.")
    else:
        print(f"Great, {new_user} is available!")


