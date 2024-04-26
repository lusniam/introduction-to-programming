print("Wyznaczę dwie największe wartości z twojego zbioru,\nPodaj dowolną ilość liczb lub wpisz koniec:")
S=[]
while(True):
    x=input()
    if x=='koniec':
        break
    else:
        try:
            x=float(x)
            S.append(x)
        except ValueError:
            print("Wpisana wartość nie jest liczbą!")
if len(S)==0:
    print("Nie podano żadnego zbioru!")
elif len(S)==1:
    print(f"Podano jedną liczbę {S[0]}, nie mogę wyznaczyć dwóch największych wartości")
else:
    max1=S[0]
    max2=S[1]
    if(max1<max2):
        max1=max2
        max2=S[0]
    for liczba in S:
        if max1<liczba:
            max2=max1
            max1=liczba
    print(f"Dwa największe elementy z twojego zbioru to {max1} i {max2}")
