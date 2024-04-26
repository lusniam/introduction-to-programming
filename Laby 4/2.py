print("Podaj dowolną ilość liczb lub wpisz 'koniec':")
S=[]
while(True):
    x=input()
    if x=='koniec':
        break
    else:
        try:
            x=float(x)
            S.append(x)
        except ValueError:
            print("Wpisana wartość nie jest liczbą!")
print("Podaj zakres, dla którego mam sprawdzić wpisane liczby:")
min=float(input("Liczba minimalna: "))
max=float(input("Liczba maksymalna: "))
zakres=0
for elem in S:
    if elem>=min and elem<=max:
        zakres+=1
print(f"W zakresie {min}/{max} znajduje się {zakres}/{len(S)} z podanych liczb")
