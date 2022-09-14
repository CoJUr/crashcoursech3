house = 'mansion'
print("Is house == 'mansion'? I predict True.")
print(house == 'mansion')
print("Is house == 'apartment'? I predict False.")
print(house == 'apartment')

computer = 'laptop'
print("\nIs computer == 'desk top'? I predict false.")
print(computer == 'desk top')
print("Is computer == 'laptop'? I predict true.")
print(computer == 'laptop')
print("Is computer == 'LAPTOP'? I predict false.")
print(computer == 'LAPTOP')
print("Is computer.lower() == 'laptop'? I predict true.")
print(computer.lower() == 'laptop')

dog = 'pug'
print("\nIs dog == 'pug'? I predict true.")
print(dog == 'pug')
print("Is dog == 'PUG'? I predict false.")
print(dog == 'PUG')
print("Is dog == 'Pug'? I predict false.")
print(dog == 'Pug')
print("Is dog.lower() == 'pug'? I predict true.")
print(dog.lower() == 'pug')
print("Is dog >= 'pu'? I predict true.")
print(dog >= 'pu')

cat = 'tabby'
print("\nIs cat == 'tabby'? I predict true.")
print(cat == 'tabby')
print("is cat == 'Tabby' or 'tabby'? I predict true.")
print((cat == 'Tabby') or (cat == 'tabby'))

list = ['cat', 'dog', 'bird']
print("\nIs 'cat' in list? I predict true.")
print('cat' in list)
print("Is 'fish' in list? I predict false.")
print('fish' in list)
print('Is dog NOT in list? I predict false.')
print('dog' not in list)