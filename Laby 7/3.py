def usun_elementy(t):
    x=min(t)
    for i in range(len(t)):
        if t[i]==x:
            t.pop(i)
            break
    x=min(t)
    for i in range(len(t)):
        if t[i]==x:
            t.pop(i)
            break
    return t

while True:
    n=input("Podaj rozmiar tablicy: ")
    try:
        n=int(n)
        break
    except ValueError:
        print("Nie podano liczby!")
t=[]
while True and len(t)!=n:
    x=input("Podaj liczbę: ")
    try:
        x=int(x)
        if x>=1 and x<=100:
            t.append(x)
    except ValueError:
        print("Nie podano poprawnej liczby!")

print("Tablica na wejsciu:",t)
if len(t)>0:
    t=usun_elementy(t)
else:
    print("Tablica nie posiada liczb!")
print("Tablica na wyjsciu:",t)