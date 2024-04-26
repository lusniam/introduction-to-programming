tab=[]
while(len(tab)<10):
    x=input("Podaj liczbę: ")
    try:
        x=int(x)
        if x==0:
            break
        tab.append(x)
    except ValueError:
        print("Nie podano liczby!")
for i in range(len(tab)):
    if tab[i]%2==0:
        continue
    else:
        for j in range(i+1,len(tab)):
            if tab[j]%2==0:
                tab[i],tab[j]=tab[j],tab[i]
                break
n=0
for i in range(len(tab)):
    if tab[i]%2==1:
        n=i
        break
for i in range(0,n):
    for j in range(i,n):
        if tab[i]>tab[j]:
            tab[i],tab[j]=tab[j],tab[i]
for i in range(n,len(tab)):
    for j in range(i,len(tab)):
        if tab[i]>tab[j]:
            tab[i],tab[j]=tab[j],tab[i]
print(f"Otrzymana tablica to {tab}")