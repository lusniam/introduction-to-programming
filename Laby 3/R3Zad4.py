liczba=int(input("Podaj liczbę: "))
lmin=liczba
lmax=liczba
while(liczba%2!=1):
    liczba=int(input("Podaj liczbę: "))
    if(liczba<lmin):
        lmin=liczba
    if(liczba>lmax):
        lmax=liczba
potega=lmin
for i in range (lmax):
    potega*=lmin
print("Najmniejsza wartość:",lmin,"\nNajwiększa wartość:",lmax,"Wynik potęgowania (min^max):",potega)