import biblioteka
# 
biblioteka.funkcja_z_biblioteki()
# 
# 
def dodawanie():
    a=int(input("podaj pierwszy składnik sumy"))
    b=int(input("podaj drugi składnik sumy"))
    c=int(input("podaj trzeci składnik sumy"))
    wynik=a+b+c
    print("suma wynosi", wynik)
  
  
def odejmowanie():
    a=int(input("podaj pierwszą liczbę"))
    b=int(input("podaj drugą liczbę"))
    c=int(input("podaj trzecią liczbę"))
    global wynik
    wynik=a-b-c
    print("wynik różnicy wynosi", wynik)

odejmowanie()
print("to jest wynik poza ciałem funkcji", wynik)


# def dodawanie(a,b=6,c=6):
#     if a==3:
#         wynik=a+b+c
#         print(wynik)
#     else:
#         print("brak obliczenia")


# dodawanie(3,2,7)




