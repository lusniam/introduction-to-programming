def obliczenie():
    a=int(input("podaj liczbe a "))
    b=int(input("podaj liczbe b "))
    global wynik
    wynik=a+b
    
    


def main():
    obliczenie()
    c=int(input("podaj liczbę c "))
    wynik2=wynik+c
    print("wynik końcowy to:", wynik2)

main()



