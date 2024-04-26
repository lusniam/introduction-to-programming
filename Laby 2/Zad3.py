x=int(input("Podaj liczbę w zakresie 0-999:"))
if(x<0 or x>999):
    print("Błąd: podano liczbę spoza zakresu")
j=int(x%10)
x/=10
d=int(x%10)
x/=10
s=int(x%10)
x=int(x*100)
print("Liczba na wejsciu:",x)
print("Suma cyfr:",j+d+s,", setki:",s,",dziesiatki: ",d,", jednosci: ",j)