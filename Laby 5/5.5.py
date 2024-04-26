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
i=0
while i<len(t):
    if t[i]%5==0:
        t.pop(i)
    else:
        i+=1
print(t)