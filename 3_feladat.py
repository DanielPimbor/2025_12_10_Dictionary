"""3.1 Feladat
Írj egy programot, amely szótárban tárol adatokat (legalább egy int, str, és bool típusút). A program a írja ki a képernyőre az adatszerkezet! 
A felhasználónak legyen lehetősége ezt az adatszerkezetet egy kulcs-érték párral bővítenie. A program végül írja ki a képernyőre a frissített adatszerkezetet! """

roli = {"Név": "Müller Gábor Roland", "Lábméret": 42, "Van-e konzolja?": True}

for kulcs, ertek in roli.items():
    print(f'{kulcs}, {ertek}')

choice = input('Szeretnél hozzáadni adatot? y/n ')

if choice == 'y':
    stuff = input('Milyen adatpontot szeretnél hozzáadni? ')
    stuff_info = input('Milyen infot tartalmaz az adatpont? ')
    roli[stuff] = stuff_info
    for kulcs, ertek in roli.items():
        print(f'{kulcs}, {ertek}')

if choice == 'n':
    print('Pápá')

