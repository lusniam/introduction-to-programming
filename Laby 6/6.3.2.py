p=0
w=0
o=0
while True:
    x=input("Podaj dodatnią podstawę potęgi: ")
    try:
        p=float(x)
        break
    except ValueError:
        print("Nie podano dodatniej liczby!")
while True:
    x=input("Podaj wykładnik potęgi: ")
    try:
        w=int(x)
        break
    except ValueError:
        print("Nie podano dodatniej liczby!")
while True:
    x=input("Podaj ogranicznik: ")
    try:
        o=float(x)
        break
    except ValueError:
        print("Nie podano dodatniej liczby!")
wynik=1
for i in range(w):
    if wynik*p<o:
        wynik*=p
    else: break
print(f"Otrzymany wynik to {wynik}")