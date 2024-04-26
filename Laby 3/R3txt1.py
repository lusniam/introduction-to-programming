from random import randint
dlugosc=int(input("Podaj długość planszy:"))
czypetla=bool(input("Czy plansza ma być zapętlona?(True/False?"))
liczbagraczy=int(input("Podaj liczbę graczy(1-4):"))
while(liczbagraczy<1 or liczbagraczy>4):
    liczbagraczy=int(input("Podaj liczbę graczy(1-4):"))
a=randint(1,dlugosc-1)
b=randint(1,dlugosc-1)
while(b==a):
    b=randint(1,dlugosc-1)
c=randint(1,dlugosc-1)
while(c==a or c==b):
    c=randint(1,dlugosc-1)
d=dlugosc
e=randint(1,dlugosc-1)
while(e==a or e==b or e==c):
    e=randint(1,dlugosc-1)
gra=bool(True)
