wynik=float(0)
op=int(1)
print("Witamy w kalkulatorze")
while(op!=0):
    print("Aktualna wartosc =",wynik)
    op=int(input("Podaj operacje (0 - wyjscie, 1 [+], 2 [-], 3 [*], 4 [/], 5[^]):"))
    if(op==1):
        liczba=float(input("Podaj liczbę do dodania:"))
        wynik+=liczba
    elif(op==2):
        liczba=float(input("Podaj liczbę do odjęcia:"))
        wynik-=liczba
    elif(op==3):
        liczba=float(input("Podaj liczbe do pomnożenia:"))
        wynik*=liczba
    elif(op==4):
        liczba=float(input("Podaj liczbe do podzielenia:"))
        if(liczba==0):
            print("Błąd!(Dzielenie przez 0)")
        else:
            wynik/=liczba
    elif(op==5):
        liczba=int(input("Podaj wykładnik potęgi:"))
        if(wynik!=0):
            pod=wynik
            wynik=1
            for i in range(abs(liczba)):
                if(liczba>0):
                    wynik*=pod
                else:
                    wynik/=pod
    elif(op<0 or op>5):
        print("Nieprawidłowe działanie!")
    print("")
print("Wynik to",wynik)
print("Dziękujemy za skorzystanie z kalkulatora!")
