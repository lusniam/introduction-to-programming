class Obliczenie_kwadrat():
    def kwadrat_pole(self,a):
        wynik_pole=a*a
        print(wynik_pole)

    def kwadrat_obwod(self,a):
        wynik_obwod=4*a
        print(wynik_obwod)

class Obliczenie_kolo(Obliczenie_kwadrat): 
    def kolo_pole(self,r):
        wynik_pole=3.14*r*r
        print(wynik_pole)
    
    def kolo_obwod(self,r):
        wynik_obwod=2*3.14*r
        print(wynik_obwod)

class Obliczenie_trojkat_prostokatny(Obliczenie_kolo):
    def trojkat_prostokatny_pole(self,a,b):
        wynik_pole=a*b*0.5
        print(wynik_pole)

    def trojkat_prostokatny_obwod(self,a,b,c):
        wynik_obwod=a+b+c
        print(wynik_obwod)
# obiekt1=Obliczenie_kwadrat()


obiekt_1=Obliczenie_trojkat_prostokatny()

obiekt_1.kwadrat_pole(16)






# obiekt_czlowiek2=Obliczenie_kolo()
# obiekt_czlowiek2.kolo_pole(2)

# obiekt_czlowiek2=Obliczenie_kwadrat()
# obiekt_czlowiek2.kwadrat_obwod(8)

# obiekt_czlowiek3=Obliczenie_trojkat_prostokatny()






# obiekt1



# obiekt1=Obliczenie_kolo()
# obiekt1.kwadrat_pole()


# obiekt5.trojkat_prostokatny_pole(4,5)

# obiekt6=Obliczenie_kolo()
# obiekt6.kolo_obwod(4)

# print(obiekt1.kwadrat_pole(5))