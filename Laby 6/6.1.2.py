while True:
    n=input("Podaj rozmiar tablicy: ")
    try:
        n=int(n)
        break
    except ValueError:
        print("Nie podano liczby!")
i=0
suma=0
while i<n:
    x=0
    while True:
        x=input("Podaj liczbę: ")
        try:
            x=int(x)
            break
        except ValueError:
            print("Nie podano liczby!")
    suma+=x*x
    i+=1
print(f"Otrzymana suma to {suma}")