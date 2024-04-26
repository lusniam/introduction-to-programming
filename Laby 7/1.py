from os import system

def dopisz(tab):
    ocena=input("Podaj ocenę: ")
    try:
        ocena=float(ocena)
        if ocena>=2 and ocena <=5:
            tab.append(ocena)
        else:
            print("Podana liczba nie jest oceną!")
    except ValueError:
        print("Podana liczba nie jest oceną!")
    return tab

def sprawdz_srednia(tab):
    if len(tab)==0:
        return False
    for i in tab:
        if i==2:
            return False
    return True

def oblicz_srednia(tab):
    if len(tab)==0:
        return
    else:
        suma=0
        for i in tab:
            suma+=i
        return suma/len(tab)

print("Operacje na ocenach:")
oceny=[]
wybor=0
while wybor!=6:
    system("cls")
    wybor=int(input("Co chcesz zrobic?\n1 - Dodanie oceny\n2 - Sprawdzenie zaliczenia\n3 - Obliczenie sredniej\n4 - Posortowanie ocen\n5 - Wyswietlenie ocen\n6 - Wyjscie z programu\n"))
    if wybor==1:
        oceny=dopisz(oceny)
    elif wybor==2:
        print("Student","ma zaliczony semestr" if sprawdz_srednia(oceny) else "nie ma zaliczonego semestru")
    elif wybor==3:
        print("Srednia studenta z podanymi ocenami wynosi",oblicz_srednia(oceny))
    elif wybor==4:
        oceny.sort()
    elif wybor==5:
        print("Aktualne oceny:",oceny)
    if wybor!=6:
        system("pause")