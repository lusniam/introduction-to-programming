min=0
suma=0
srednia=0
while True:
    n=input("Podaj liczbę: ")
    try:
        n=int(n)
    except ValueError:
        print("Nie podano liczby!")
        continue
    if n%10==0:
        break
    if suma==0:
        min=n
    elif min>n:
        min=n
    suma+=n
    srednia+=1
print(f"Najmniejsza liczba to {min}, a średnia liczb to {suma/srednia}")