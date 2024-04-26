from math import sqrt

def bubble(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-i-1):
            if tab[j+1]<tab[j]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    return tab

def sito(liczba):
    tab=[True]*(liczba-1)
    i=2
    while(i<sqrt(liczba)):
        if(tab[i-2]):
            j=i*2
            while j<=liczba:
                tab[j-2]=False
                j+=i
        i+=1
    return tab
