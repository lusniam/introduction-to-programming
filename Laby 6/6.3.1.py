t=[]
while True:
    x=input("Podaj liczbę: ")
    try:
        x=float(x)
        if x==0:
            break
        t.append(x)
    except ValueError:
        print("Nie podano liczby!")
suma=0
for i in t:
    if i<t[0]:
        suma+=i
print(f"Suma liczb mniejszych od {t[0]} jest równa {suma}")