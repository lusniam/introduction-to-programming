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
        x=float(x)
        t.append(x)
        if len(t)==n:
            break
    except ValueError:
        print("Nie podano liczby!")
x=t[n-1]
suma=0
srednia=0
for i in t:
    if i>x:
        suma+=i
        srednia+=1
if srednia==0:
    print("Ostatnia liczba jest największą liczbą, nie mogę obliczyć średniej, a suma wynosi 0")
else:
    print(f"Suma z podanych liczb jest równa {suma}, a średnia {suma/srednia}")
