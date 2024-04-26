print("Podam dwie największe sumy trzech kolejnych liczb z podanej tablicy")
S=[]
while(True):
    print(f"\nMoc tablicy: {len(S)}")
    print("Podaj liczbę: " if len(S)<4 else "Podaj liczbę, lub wpisz 'koniec':")
    x=input()
    if x=='koniec':
        if len(S)<4:
            print("Zbiór nie zawiera wymaganej ilości liczb! Podaj więcej liczb!")
        else:
            break
    else:
        try:
            x=float(x)
            S.append(x)
        except ValueError:
            print("Wpisana wartość nie jest liczbą!")
suma1,suma2=0,0
i1,i2=0,0
for i in range(2,len(S)):
    suma=S[i]+S[i-1]+S[i-2]
    if suma>suma1:
        suma2=suma1
        i2=i1
        suma1=suma
        i1=i-2
print(f"Największa suma trzech liczb to {suma1} w indeksie {i1}, a druga największa to {suma2} w indeksie {i2}")