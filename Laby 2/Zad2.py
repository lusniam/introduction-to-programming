x1=float(input("Podaj 3 dodatnie liczby:"))
x2=float(input())
x3=float(input())
if(x1<=0 or x2<=0 or x3<=0):
    print("Błąd: podano liczbę niedodatnią")
else:
    print(max(x1,x2,x3))