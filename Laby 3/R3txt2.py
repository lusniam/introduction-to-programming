from random import randint
p1 = int(0)
p2 = int(0)
asy1 = int(0)
asy2 = int(0)
print("Zaczynamy w grę Oczko")
g1 = True
g2 = True
while(True):
    if(g1):
        print("\nGracz 1, masz",p1,"punktów")
        los = input("Losujesz czy rezygnujesz?(l/r)")
        if(los=='l'):
            karta=randint(2,14)
            if(karta==14):
                kartas="As"
                karta=11
                asy1+=1
            elif(karta<11):
                kartas=karta
            else:
                if(karta==13):
                    kartas='Król'
                elif(karta==12):
                    kartas='Dama'
                else:
                    kartas='Walet'
                karta-=9
            p1+=karta
            print("Wylosowana karta:",kartas)
        print("Masz",p1,"punktów")
        if(los=='r' or p1>21):
            g1=False
    if(g2):
        print("\nGracz 2, masz",p2,"punktów")
        los = input("Losujesz czy rezygnujesz?(l/r)")
        if(los=='l'):
            karta=randint(2,14)
            if(karta==14):
                kartas="As"
                karta=11
                asy2+=1
            elif(karta<11):
                kartas=karta
            else:
                if(karta==13):
                    kartas='Król'
                elif(karta==12):
                    kartas='Dama'
                else:
                    kartas='Walet'
                karta-=9
            p2+=karta
            print("Wylosowana karta:",kartas)
        print("Masz",p2,"punktów")
        if(los=='r' or p2>21):
            g2=False
    if(not(g1 or g2)):
        break
if(p1==p2 and ((asy1!=2 and asy2!=2) or (asy1==2 and asy2==2))):
    print("Remis")
elif((p1==22 and asy1==2) or (p1>p2 and p1<22) or (p1<p2 and (p1>21 or p2>21))):
    print("Wygrywa gracz 1 z wynikiem",p1,"punktów")
else:
    print("Wygrywa gracz 2 z wynikiem",p2,"punktów")