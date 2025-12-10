"""2. Feladat
Írj egy programot, amely szótárban tárolja egy macska nevét, korát. 
A felhasználónak legyen lehetősége megváltoztatni az egyik tárolt adatot. 
A program írja ki a felhasználó választása alapján az egyik adatot, kérdezze meg, mire módosítsa, végül írja ki a képernyőre a frissített adatszerkezetet!
"""

cat_name = input("Name of your cat: ")
cat_age = input("Age of your cat: ")

cat = {"name": cat_name, "age": cat_age}

print(f'This is your cats name: {cat["name"]}')
print(f'This is your cats age: {cat["age"]}')


while True:
    choice = input('Do you want to change the informations? y/n ')

    if choice == 'y':
        choice2 = input('Which one? (name/age)')
        if choice2 == 'name':
            new_name = input('Write here the new name: ')
            cat["name"] = new_name

        if choice2 == "age":
            new_age = input('Write here the new age: ')
            cat["age"] = new_age
        print('Here is your data:')
        for kulcs, ertek in cat.items():
            print(f'{kulcs}, {ertek}')


    elif choice == 'n':
        print('Here is your data:')
        for kulcs, ertek in cat.items():
            print(f'{kulcs}, {ertek}')
        break