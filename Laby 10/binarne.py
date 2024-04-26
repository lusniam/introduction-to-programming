from math import trunc

def binfind(tab,liczba):
    a=0
    o=len(tab)-1
    wynik=False
    while(not(wynik)):
        if a==o:
            i=a
        else:
            i=trunc((o-a)/2)
        if tab[i]==liczba:
            wynik=True
        elif a!=o:
            if tab[i]>liczba:
                o=i
            else:
                a=i
        else:
            break
    return wynik