print("Podaj dowolną ilość liczb różnych od zera:")
S=[]
while(True):
    x=input()
    if x=='0':
        break
    else:
        try:
            x=float(x)
            S.append(x)
        except ValueError:
            print("Wpisana wartość nie jest liczbą!")
S.sort()
x=0
liczby=""
for i in range(1,len(S)):
    if S[i]==S[i-1]:
        if x==0:
            liczby+=(f"{S[i]},")
        x+=1
        liczby+=(f"{S[i]},")
    else:
        x=0
print(f"Elementy, które się powtarzają: {liczby}")
        