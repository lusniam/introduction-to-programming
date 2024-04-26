while True:
    n=input("Podaj rozmiar tablicy: ")
    try:
        n=int(n)
        break
    except ValueError:
        print("Nie podano liczby!")
t=[]
while True and len(t)!=n:
    x=input("Podaj liczbę: ")
    try:
        x=int(x)
        if x>=1 and x<=100:
            t.append(x)
    except ValueError:
        print("Nie podano liczby!")
maxciag,maxindeks=0,0
if n==1:
    maxciag=1
for i in range(len(t)-1):
    ciag=1
    for j in range(i,len(t)-1):
        if t[j]>t[j+1]:
            break
        else:
            ciag+=1
    if ciag>maxciag:
        maxciag,maxindeks=ciag,i
print(f"Najdłuższy ciąg ma długość {maxciag} przy indeksie {maxindeks}")