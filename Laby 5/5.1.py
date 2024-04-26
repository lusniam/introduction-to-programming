from os import system

def srednia():
    s=False
    n=0
    suma=0
    while True:
        x=input("Podaj liczbę: ")
        try:
            x=float(x)
        except ValueError:
            print("Nie podano liczby!")
            continue
        if x==0:
            s=not(s)
            print("Tryb liczenia średniej jest","włączony." if s else "wyłączony.")
        elif s:
            suma+=x
            n+=1
        elif x<0:
            break
    if n==0:
        return "Nie podano żadnych liczb podczas trybu liczenia średniej!"
    else:
        return f"Otrzymano średnią {suma/n}"

while True:
    system("clear")
    print(srednia())
    if input("Wpisz 'exit' aby wyjść, inaczej program zostanie powtórzony: ")=='exit':
        break
