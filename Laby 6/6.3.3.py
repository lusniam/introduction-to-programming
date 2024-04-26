min1,min2=501,501
while True:
    x=input("Podaj liczbę: ")
    try:
        x=float(x)
        if x>500 or x<10:
            break
        if x<min1:
            min1,min2=x,min1
        elif x<min2:
            min2=x
    except ValueError:
        print("Nie podano liczby!")
print("Nie podano żadnej liczby w przedziale!" if min1==501 else f"Podano jedną liczbę {min1}" if min2==501 else f"Dwie najmniejsze liczby z podanych to {min1} i {min2}")