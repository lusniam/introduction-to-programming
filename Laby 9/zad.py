import funkcje
from os import system

wybor=0
while True:
    wybor=input("1-sortowanie\n2-sito\n")
    try:
        wybor=int(wybor)
        if wybor==1 or wybor==2:
            break
    except ValueError:
        system("cls")
t=[]
if wybor==1:
    while True:
        liczba=input("Podaj liczbe, lub wpisz 0: ")
        try:
            liczba=float(liczba)
            if liczba==0:
                break
            t.append(liczba)
        except ValueError:
            print("Nie podano liczby!")

    print("Podano tabele:",t)
    print("Tabela po sortowaniu:",funkcje.bubble(t))
else:
    while True:
        wybor=input("Podaj liczbe, do ktorej mam wyliczyc liczby pierwsze: ")
        try:
            wybor=int(wybor)
            break
        except ValueError:
            system("cls")
    t=funkcje.sito(wybor)
    for i in range(len(t)):
        print("Liczba",i+2,"jest" if t[i] else "nie jest","pierwsza")
    
t=input()