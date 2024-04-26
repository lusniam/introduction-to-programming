from os import system

def sprawdz_wybor():
    global wybor
    if wybor>0 and wybor<4:
        obsluz_tabele()
        system("pause")

def obsluz_tabele():
    global tab,wybor
    if wybor==3:
        print("Aktualna tabela:",tab)
        return
    edytuj()

def edytuj():
    global tab,wybor
    if wybor==1:
        tab.append(input("Podaj element do dodania:"))
        return
    usun()

def usun():
    global tab
    if len(tab)!=0:
        tab.pop()
        return
    print("Tablica jest pusta!")

tab=[]
wybor=0
while wybor!=4:
    system("cls")
    wybor=int(input("Co chcesz zrobic?\n1-Dopisac element\n2-Usunac ostatni element\n3-Wyswietlic tablice\n4-Wyjsc z programu\n"))
    sprawdz_wybor()