sym1=3
sym2=3
while(sym1<0 or sym1>2 or sym2<0 or sym2>2 or sym1==sym2):
    sym1=int(input("Gracz 1, podaj swój symbol(0-papier,1-kamień,2-nożyce):"))
    sym2=int(input("Gracz 2, podaj swój symbol(0-papier,1-kamień,2-nożyce):"))
    print("Wynik: ")
    if(sym1==sym2):
        print("Remis, powtarzamy grę")
    elif(sym2-1==sym1 or sym1-2==sym2):
        print("Wygrana gracza 1")
    elif(sym1-1==sym2 or sym2-2==sym1):
        print("Wygrana gracza 2")
    else:
        print("Podano niewłaściwe liczby, powtarzamy grę")