from math import sqrt
print("Znajdę pierwiastki równania a*x^2+b*x+c=0")
a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
c=float(input("Podaj c: "))
delta=pow(b,2)-4*a*c
if(delta<0):
    print("Brak pierwiastków")
elif(delta==0):
    print("x0 =",-b/2/a)
else:
    print("x1 =",(-b+sqrt(delta))/2/a,"oraz x2 =",(-b-sqrt(delta))/2/a)