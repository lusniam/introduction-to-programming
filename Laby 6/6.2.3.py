while True:
    n=input("Podaj rozmiar tablicy (musi być to liczba parzysta większa od 0): ")
    try:
        n=int(n)
        if n>0 and n%2==0:    
            break
    except ValueError:
        print("Nie podano liczby!")
t=[]
while True:
    x=input("Podaj liczbę: ")
    try:
        x=float(x)
        t.append(x)
        if len(t)==n:
            break
    except ValueError:
        print("Nie podano liczby!")
print(f"Średnia dwóch środkowych liczb to {(t[int((n/2)-1)]+t[int(n/2)])/2}")