tab=[]
while(len(tab)<4):
    x=input("Podaj liczbę dodatnią: ")
    try:
        x=int(x)
        if x>0:
            tab.append(x)
    except ValueError:
        print("Nie podano liczby!")
for i in range(len(tab)-1):
    tab[i]/=tab[3]
tab.pop()
print(tab)