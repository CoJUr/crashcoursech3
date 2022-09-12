dream_guests = ['Stephen Hawking', 'Kobe Bryant', 'Michael Jackson', 'Elon Musk', 'Albert Einstein']
print(f"Hello {dream_guests[0]}, {dream_guests[1]}, {dream_guests[2]}, {dream_guests[3]}, and {dream_guests[4]}! I'd "
      f"like to invite you all to dinner.")

print(f"Unfortunately, {dream_guests[2]} had to decline the invitation.")

dream_guests.pop(2)
print(dream_guests)
dream_guests.insert(2, 'Michael Jordan')

print(f"Hello {dream_guests[0]}, you are once again invited to dinner.")
print(f"Hello {dream_guests[1]}, you are once again invited to dinner.")
print(f"Hello {dream_guests[2]}, you are invited to dinner ienstead of the King of Pop.")
print(f"Hello {dream_guests[3]}, you are once again invited to dinner.")
print(f"Hello {dream_guests[4]}, you are once again invited to dinner.")

print(f"""Dear {dream_guests[0]},
{dream_guests[1]},
{dream_guests[2]},
{dream_guests[3]},
{dream_guests[4]},
I've found a bigger table, so I'm inviting more people!""")

dream_guests.insert(0, 'Abe Lincoln')
dream_guests.insert(2, 'Billy Mays')
dream_guests.append('Pope Francis')

print(f"""Dear {dream_guests[0]}
{dream_guests[1]}, 
{dream_guests[2]}, 
{dream_guests[3]}, 
{dream_guests[4]}, 
{dream_guests[5]}, 
{dream_guests[6]}, 
{dream_guests[7]},
you are invited to dinner.""")

print(f"All, I'm sorry, but I can only invite two people to dinner.")
pop_number_1 = dream_guests.pop(0)
print(f"Sorry, {pop_number_1}, you're un-invited.")
pop_number_2 = dream_guests.pop(1)
print(f"Sorry, {pop_number_2}, you're un-invited.")
pop_number_3 = dream_guests.pop(2)
print(f"Sorry, {pop_number_3}, you're un-invited.")
pop_number_4 = dream_guests.pop(3)
print(f"Sorry, {pop_number_4}, you're un-invited.")
pop_number_5 = dream_guests.pop(2)
print(f"Sorry, {pop_number_5}, you're un-invited.")
pop_number_6 = dream_guests.pop(2)
print(f"Sorry, {pop_number_5}, you're un-invited.")

#
print(dream_guests)
#
amount_of_guests = len(dream_guests)
print(amount_of_guests)
print(f"In total, " + str(amount_of_guests) + " guests are still invited to dinner.")
