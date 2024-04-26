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
symetria=False
for i in range(int(len(S)/2)):
    symetria=S[i]!=S[len(S)-1-i]
    if symetria:
        break
print("Podana tablica","nie jest" if symetria else "jest","symetryczna względem jej środka")