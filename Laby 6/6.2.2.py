p=0
w=0
while True:
    p=input("Podaj podstawę potęgi: ")
    try:
        p=float(p)
        break
    except ValueError:
        print("Nie podano liczby!")
while True:
    w=input("Podaj wykładnik potęgi: ")
    try:
        w=int(w)
        break
    except ValueError:
        print("Nie podano liczby całkowitej!")
potega=1
for i in range(abs(w)):
    if w>0:
        potega*=p
    else:
        potega/=p
print(f"{p} do potęgi {w} jest równe {potega}.")