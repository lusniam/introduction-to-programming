from math import log2

def MINMAX(S):
    if len(S)==2:
        return min(S[0],S[1]),max(S[0],S[1])
    a=[]
    b=[]
    for i in range(int(len(S)/2)):
        a.append(S[i])
        b.append(S[int(i+(len(S)/2))])
    A=MINMAX(a)
    B=MINMAX(b)
    return [min(A[0],B[0]),max(A[1],B[1])]

def main():
    print("Wyznaczę minimalny i maksymalny element zbioru, który podasz")
    print("Pamiętaj, że zbiór musi mieć n elementów, gdzie n jest potęgą liczby 2 i n>1")
    S=[]
    while(True):
        wyjscie=len(S)>1 and log2(len(S))%1==0
        print(f"\nMoc zbioru: {len(S)},","możesz zakończyć wpisywanie liczb!" if wyjscie else "")
        print("Podaj liczbę, lub wpisz 'koniec' aby zakończyć wpisywanie liczb: " if wyjscie else "Podaj liczbę: ")
        x=input()
        if x=='koniec':
            if wyjscie:
                break
            else:
                print("Zbiór nie zawiera wymaganej ilości liczb! Podaj więcej liczb!")
        else:
            try:
                x=float(x)
                S.append(x)
            except ValueError:
                print("Wpisana wartość nie jest liczbą!")
    A=MINMAX(S)
    print(f"\nWartość najmniejsza to {A[0]}, a największa to {A[1]}")

if __name__=='__main__':
    main()