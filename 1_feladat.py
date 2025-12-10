"""1. Feladat
Írj egy programot, amely a felhasználótól bekéri egy kutya nevét, életkorát, fajtáját, 
és azt hogy rendelkezik-e érvényes oltással veszettség ellen! 
Az adatokat tárolja a program szótárban, és írja ki a képernyőre az adatszerkezetet! """

kutya_nev =input('Add meg a kutya nevét: ')
kutya_kor = input('Add meg a kutya korát: ')
kutya_fajta = input('Add meg a kutya fajtáját: ')
oltas_valasz = input('Rendelkezik a kutya oltással? i/n ')
oltas = oltas_valasz == 'i' or oltas_valasz == 'igen'


kutya ={
    "nev": kutya_nev,
    "kor": kutya_kor,
    "fajta": kutya_fajta,
    "oltas": oltas
}


for kulcs, ertek in kutya.items():
    print(f'{kulcs}, {ertek}')