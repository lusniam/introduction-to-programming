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
        if x>=1 and x<=100:
            t.append(x)
        if len(t)==n:
            break
    except ValueError:
        print("Nie podano liczby!")
t.sort()
para=False
for i in range(len(t)-1):
    if t[i]==t[i+1]:
        para=True
        break
print("Tak," if para else "Nie, nie","istnieje para takich samych liczb")