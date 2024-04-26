from random import randint
print("Witamy na loterii!\nPodaj 6 różnych liczb z przedziału 1-40.")
S=[]
while len(S)!=6:
    x=input("Podaj liczbę: ")
    try:
        x=int(x)
        if x<1 or x>40:
            print("Nie podano liczby z podanego przedziału!")
        elif x in S:
            print("Podano już taką liczbę! Podaj inną!")
        else:
            S.append(x)
    except ValueError:
        print("Nie podano liczby całkowitej z podanego przedziału!")
S.sort()
W=[]
while len(W)!=6:
    x=randint(1,40)
    if x not in W:
        W.append(x)
W.sort()
print("Twoje liczby:",S)
print("Wygrywające liczby:",W)
wygrana=0
for i in S:
    if i in W:
        wygrana+=1
print(f"Trafiłeś {wygrana} liczb!")
if wygrana==4:
    wygrana=50
elif wygrana==5:
    wygrana==400
elif wygrana==6:
    wygrana==2000
print(f"Wygrywasz {wygrana}zł!" if wygrana>3 else "Nic nie wygrywasz! Spróbuj szczęścia jeszcze raz!")