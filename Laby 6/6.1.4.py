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
suma=0
ip=0
for i in range(len(t)-2):
    nsuma=t[i]+t[i+1]+t[i+2]
    if nsuma>suma:
        suma=nsuma
        ip=i
print(f"Indeks początkowy największej sumy to {ip}")