srednia=0
iloczyn=1
suma=0
while(suma<=255 and iloczyn<=50000):
    liczba=float(input("Podaj liczbę:"))
    suma+=liczba
    iloczyn*=liczba
    srednia=(srednia*2+liczba)/2
print("Średnia arytmetyczna wpisanych liczb jest równa",srednia)