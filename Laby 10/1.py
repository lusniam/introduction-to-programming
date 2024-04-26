from binarne import binfind

def posortuj_dane(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-i-1):
            if tab[j+1]<tab[j]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    return tab

tab=[]
dane=open("Python\Lab9\liczby.txt","r")
tab_dane=dane.read().split("\n")
for i in tab_dane:
    tab.append(int(i))
dane.close()

tab=posortuj_dane(tab)

wynik=open("Python\Lab9\wynik.txt","w")
for i in tab:
    wynik.write(str(i)+"\n")
wynik.close()

print("Szukana liczba","znajduje" if binfind(tab,int(input("Podaj liczbę: "))) else "nie znajduje","się w tablicy")