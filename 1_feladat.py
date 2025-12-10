ures_szotar = {}

szemely = {
    "nev": "Kis Ferenc",
    "kor": 16,
    "telefon": "06706646767",
    "varos": "Szekszárd"

}

#kulcsok
print(szemely["nev"])
print(szemely["kor"])
print(szemely.get("kor"))



#print(szemely["telefon"])
print(szemely.get("telefon", "Nincs a szótárban ilyen elem."))


#érték módosítása
szemely["kor"] = 17
print(szemely["kor"])

#kulcsértékpár hozzáadaása
szemely["neme"] = "vicces"
print(szemely["neme"])

#del kulcs
print(szemely["varos"])
del szemely["varos"]
print(szemely.get("varos", "Nincs a szótárban ez a kulcs."))

#in operator
if "nev" in szemely:
    print('A keresett kulcs megtalálható a szótárban.')

if "bankszamla" not in szemely:
    print('A keresett kulcs nem található.')


#kulcsérték párok

for kulcs, ertek in szemely.items():
    print(f'{kulcs}, {ertek}')