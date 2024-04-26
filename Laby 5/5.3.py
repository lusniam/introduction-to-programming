while True:
    n=input("Podaj rozmiar tablicy: ")
    try:
        n=int(n)
        break
    except ValueError:
        print("Nie podano liczby!")
t=[]
while True:
    x=input("Podaj liczbę: ")
    try:
        x=int(x)
        t.append(x)
        if len(t)==n:
            break
    except ValueError:
        print("Nie podano liczby!")
o=t[n-1]
s=[]
for liczba in t:
    suma=0
    i=liczba
    while i>0:
        suma+=i%10
        i=int(i/10)
    if suma>o:
        s.append(liczba)
print(f"Wśród podanych liczb znaleziono {len(s)} spełniających warunki")