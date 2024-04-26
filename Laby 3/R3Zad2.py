from random import randint
n=int(input("Podaj ilość liczb do wylosowania: "))
suma=0
for i in range(n):
    liczba=int(randint(10,50))
    suma+=int(pow(liczba,2))
    print("Wylosowano liczbę",liczba)
print("Suma kwadratów wylosowanych liczb jest równa",suma)