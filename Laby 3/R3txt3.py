from random import randint
from math import ceil
from os import system

maxhp=int(50)
akthp=int(maxhp)
zloto=int(5)
poziom=int(1)
exp=int(0)
napoje=int(0)
minatak=int(2)
maxatak=int(10)
pmiecza=int(1)
pzbroi=int(0)

def wstep():
	print("Witaj w Mieczach i Kaloszach!\nJesteś gladiatorem, twoim zadaniem jest pokonać bossa areny.")
	print("Walcz z przeciwnikami, aby zdobywać złoto i doświadczenie!")
	print("Tawerna oferuje noclegi, dzięki którym odnowisz swoje zdrowie!")
	print("Zajdź do handlarza aby kupić uzbrojenie lub mikstury lecznicze, które pomogą ci podczas walki!")
	print("\nOto statystyki twojego gladiatora:")
	print(f"\nMasz {akthp}/{maxhp} punktów zdrowia.")
	print(f"Twoje ataki zadają {minatak}-{maxatak} punktów obrażeń.")
	print(f"Masz {poziom} poziom doświadczenia.")
	BrakExp()
	print(f"Masz {zloto} sztuk złota oraz {napoje} mikstur leczniczych.")
	print("\nWychodzisz na główną ulicę miasta, gotowy rozpocząć swoją przygodę.")
	input("\nNaciśnij enter.")

def tawerna():
	system("cls")
	global zloto,akthp,maxhp
	if zloto<50:
		print("Koszt przespania się w tawernie to 50 sztuk złota, noc w tawernie w pełni odnawia twoje zdrowie.")
		print("Masz za mało złota, aby to zrobić.")
	else:
		ch=0
		while True:
			print("Koszt przespania się w tawernie to 50 sztuk złota, noc w tawernie w pełni odnawia twoje zdrowie.")
			print("Czy chcesz przespać się w tawernie?(Tak/Nie)")
			ch=input("")
			system("cls")
			if ch=="Tak":
				zloto-=50
				akthp=maxhp
				print("Przespałeś się w tawernie, twoje zdrowie zostało odnowione!")
				break
			elif ch=="Nie":
				return
	input("\nNaciśnij enter.")

def potka():
	global zloto,napoje
	system("cls")
	if zloto<20:
		print("Mikstura lecząca kosztuje 20 sztuk złota i leczy około 50% maksymalnego zdrowia.")
		print("Masz za mało złota, aby to kupić.")
	else:
		if napoje<4:
			while True:
				print("Mikstura lecząca leczy około 50% maksymalnego zdrowia.")
				print("Czy chcesz kupić miksturę leczącą za 20 sztuk złota?(Tak/Nie)")
				ch=input("")
				system("cls")
				if ch=="Tak":
					zloto-=20
					napoje+=1
					print(f"Kupiłeś jedną miksturę, aktualnie masz ich {napoje}.")
					break
				elif ch=="Nie":
					return
		else:
			print("Masz maksymalną liczbę mikstur!")
	input("\nNaciśnij enter.")

def miecz():
	global pmiecza,zloto,minatak,maxatak
	system("cls")
	if pmiecza<4:
		koszt=int(125*pow(2,pmiecza))
		if zloto<koszt:
			print(f"Poziom twojego miecza to {pmiecza}.")
			print("Każdy poziom miecza dodaje 2-3 do twojego ataku!")
			print(f"Miecz następnego poziomu kosztuje {koszt}.")
			print("Masz za mało złota, aby to kupić.")
		else:
			while True:
				print(f"Poziom twojego miecza to {pmiecza}.")
				print("Każdy poziom miecza dodaje 2-3 do twojego ataku!")
				print(f"Miecz następnego poziomu kosztuje {koszt}.")
				print(f"Czy chcesz kupić miecz poziomu {pmiecza+1} za {koszt} sztuk złota?(Tak/Nie)")
				ch=input()
				system("cls")
				if ch=="Tak":
					zloto-=koszt
					pmiecza+=1
					minatak+=2
					maxatak+=3
					print(f"Kupiłeś miecz poziomu {pmiecza}!\nTwoje ataki zadają teraz {minatak}-{maxatak}")
					break
				elif ch=="Nie":
					pmiecza-=1
					return
	else:
		print("Posiadasz już maksymalny poziom miecza!")
	input("\nNaciśnij enter.")

def zbroja():
	global pzbroi,zloto,maxhp,akthp
	system("cls")
	if pzbroi<3:
		koszt=int(250*pow(2,pzbroi))
		if zloto<koszt:
			print(f"Poziom twojej zbroi to {pzbroi}.")
			print("Każdy poziom zbroi dodaje 10 do twojego maksymalnego zdrowia!")
			print(f"Zbroja następnego poziomu kosztuje {koszt}.")
			print("Masz za mało złota, aby to kupić.")
		else:
			while True:
				print(f"Poziom twojej zbroi to {pzbroi}.")
				print("Każdy poziom zbroi dodaje 10 do twojego maksymalnego zdrowia!")
				print(f"Zbroja następnego poziomu kosztuje {koszt}.")
				print(f"Czy chcesz kupić zbroję poziomu {pzbroi+1} za {koszt} sztuk złota?(Tak/Nie)")
				ch=input("")
				system("cls")
				if ch=='Tak':
					zloto-=koszt
					maxhp+=10
					akthp+=10
					pzbroi+=1
					print(f"Kupiłeś zbroję poziomu {pzbroi}!\nTwoje maksymalne zdrowie wzrosło do {maxhp}!")
					break
				elif ch=="Nie":
					pzbroi-=1
					return
	else:
		print("Posiadasz już maksymalny poziom zbroi!")
	input("\nNaciśnij enter.")

def sklep():
	while True:
		system("cls")
		print(f'Witaj w sklepie, co cię interesuje?')
		wsklep=input(f'Masz {zloto} sztuk zlota\nWpisz "Miecz", "Zbroja", "Mikstura", lub "Powrót", aby wrócić na ulicę.\n')
		if wsklep == 'Powrót':
			return
		elif wsklep=="Miecz":
			miecz()
		elif wsklep=="Zbroja":
			zbroja()
		elif wsklep=="Mikstura":
			potka()

def BrakExp():
	global poziom,exp
	print(f"Masz {exp} punktów doświadczenia.")
	if poziom<4:
		print(f"Brakuje ci {int(500*pow(poziom-1,2)+125-exp)} doświadczenia do poziomu {poziom+1}.")
	else:
		print("Masz maksymalny poziom!")

def CheckLvl():
	global exp,poziom,maxhp,akthp,minatak,maxatak
	if (poziom==1 and exp>=125) or (poziom==2 and exp>=625) or (poziom==3 and exp>=2125):
		exp=0
		poziom+=1
		maxhp+=10
		akthp=maxhp
		minatak+=2
		maxatak+=2
		print(f"Gratulacje! Osiągnąłeś {poziom} poziom doświadczenia!")
		print(f"Twoje maksymalne zdrowie wzrasta o 10! Aktualnie masz go {maxhp}.")
		print(f"Twoje ataki zadają 2 punkty obrażeń więcej! Aktualnie {minatak}-{maxatak}!")
	else:
		BrakExp()

def statystyki():
	global akthp,maxhp,minatak,maxatak,poziom,zloto,napoje,pmiecza,pzbroi
	system("cls")
	print(f"Masz {akthp}/{maxhp} punktów zdrowia.")
	print(f"Twoje ataki zadają {minatak}-{maxatak} punktów obrażeń.")
	print(f"Masz {poziom} poziom doświadczenia.")
	BrakExp()
	print(f"Masz {zloto} sztuk złota oraz {napoje} mikstur leczniczych.")
	print(f"Posiadasz miecz poziomu {pmiecza}.")
	if pzbroi==0:
		print("Nie posiadasz zbroi.")
	else:
		print(f"Posiadasz zbroję poziomu {pzbroi}.")
	input("\nNaciśnij enter.")

def debug():
	global akthp,maxhp,minatak,maxatak,poziom,zloto,napoje,pmiecza,pzbroi,exp
	print("wpisz z aby zmienic statystyke")
	x=input("maxhp")
	if x=='z':
		maxhp=int(input(""))
	x=input("akthp")
	if x=='z':
		akthp=int(input(""))
	x=input("zloto")
	if x=='z':
		zloto=int(input(""))
	x=input("poziom")
	if x=='z':
		poziom=int(input(""))
	x=input("exp")
	if x=='z':
		exp=int(input(""))
	x=input("napoje")
	if x=='z':
		napoje=int(input(""))
	x=input("minatak")
	if x=='z':
		minatak=int(input(""))
	x=input("maxatak")
	if x=='z':
		maxatak=int(input(""))

def walka():
	global akthp,maxhp,minatak,maxatak,poziom,zloto,napoje,exp
	system("cls")
	while True:
		print("Wchodzisz na arenę. Dostępni przeciwnicy:")
		if poziom<=2:
			print("-Przeciwnik normalny (Dostępny dla poziomów 1-2)")
		if poziom>=2 and poziom<=3:
			print("-Przeciwnik trudny (Dostępny dla poziomów 2-3)")
		if poziom>=3:
			print("-Boss (Dostępny dla poziomów 3-4)")
		trudnosc=input('Wybierz przeciwnika wpisując "Normalny", "Trudny", "Boss", lub "Powrót", aby wrócić do miasta:\n')
		system("cls")
		if trudnosc=="Powrót":
			return
		if (poziom>0 and poziom<3 and trudnosc =="Normalny") or (poziom>1 and poziom<4 and trudnosc =="Trudny") or (poziom>2 and trudnosc =="Boss"):
			break
	system("cls")
	if trudnosc=="Normalny":
		hpopp=randint(40,55)
		atkminopp=randint(1,3)
		atkmaxopp=randint(8,11)
		potkiopp=randint(0,1)
	elif trudnosc=="Trudny":
		hpopp=randint(80,100)
		atkminopp=randint(8,10)
		atkmaxopp=randint(16,18)
		potkiopp=randint(0,2)
	elif trudnosc=="Boss":
		hpopp=125
		atkminopp=18
		atkmaxopp=28
		potkiopp=4
	hpmaxopp=hpopp
	tura=randint(0,1)
	if tura==0:
		tura="gracz"
	else:
		tura="przeciwnik"
	print(f"Statystyki przeciwnika:\nZdrowie: {hpopp}\nObrażenia: {atkminopp}-{atkmaxopp}\nPojedynek rozpocznie {tura}\nWalka!\n")
	while True:
		print(f"Masz {akthp}/{maxhp} punktów zdrowia, przeciwnik ma {hpopp}/{hpmaxopp} punktów zdrowia")
		if tura=="gracz":
			print(f"\nAktualne zdrowie: {akthp}/{maxhp}")
			while True:
				ch=input('Wpisz "Atak", aby zaatakować, lub "Mikstura" aby się uleczyć!\n')
				if ch=="Atak":
					atak=randint(minatak,maxatak)
					hpopp-=atak
					print(f"\nZadano {atak} punktów obrażeń przeciwnikowi!")
					break
				elif ch=="Mikstura":
					if napoje>0:
						leczenie=int(ceil(maxhp*(40+randint(0,20))/100))
						print(f"\nUleczono {leczenie} punktów zdrowia!")
						akthp+=leczenie
						napoje-=1
					else:
						print("\nBrak mikstur leczniczych! Przeciwnik wykorzystuje okazję!")
					break
			if(hpopp<=0):
				wynik='w'
				break
			tura="przeciwnik"
		else:
			if hpopp/hpmaxopp<0.5 and potkiopp>0 and randint(1,10)<2:
				leczenie=int(ceil(hpmaxopp*(40+randint(0,20))/100))
				print(f"\nPrzeciwnik używa mikstury leczenia, uleczono {leczenie} punktów zdrowia!")
				hpopp+=leczenie
				potkiopp-=1
			else:
				atak=randint(atkminopp,atkmaxopp)
				akthp-=atak
				print(f"\nPrzeciwnik atakuje! Otrzymujesz {atak} punktów obrażeń!")
			if(akthp<=0):
				wynik='p'
				break
			tura="gracz"
	print(f"Wygrywa {tura}!")
	if wynik=="w":
		if trudnosc=="Boss":
			print("Pokonałeś bossa areny!")
			poziom=5
			return
		elif trudnosc=="Trudny":
			mnoznik=int(3)
		else:
			mnoznik=int(1)
		ZdobytyExp=mnoznik*randint(100,200)
		ZdobyteZloto=mnoznik*randint(150,250)
		exp+=ZdobytyExp
		zloto+=ZdobyteZloto
		print(f"Za wygraną otrzymujesz {ZdobytyExp} punktów doświadczenia oraz {ZdobyteZloto} złota!")
		CheckLvl()
	input("Naciśnij enter.")

wstep()
while True:
	system("cls")
	print('Co zamierzasz zrobić? Wpisz:\n-"Arena", aby pojść na walkę,\n-"Tawerna", aby skorzystać z tawerny,\n-"Mikstura", aby wypić miksturę leczniczą\n-"Sklep", aby kupić nowe przedmioty,\n-"Statystyki", aby zobaczyć swoje statystyki')
	wybor=input()
	if wybor=="Arena":
		walka()
	elif wybor=="Tawerna":
		tawerna()
	elif wybor=="Mikstura":
		if napoje>0:
			leczenie=int(ceil(maxhp*(35+randint(0,20))/100))
			if leczenie>maxhp-akthp:
				leczenie=maxhp-akthp
			print(f"Uleczono {leczenie} punktów zdrowia!")
			akthp+=leczenie
			napoje-=1
		else:
			print("Brak mikstur leczniczych! Kup więcej w sklepie!")
		input("Naciśnij enter.")
	elif wybor=="Sklep":
		sklep()
	elif wybor=="Statystyki":
		statystyki()
	elif wybor=="debug":
		debug()
	if akthp<=0:
		print("Zginąłeś. Zagraj jeszcze raz!")
		break
	elif poziom==5:
		print("Gratulacje! Zostałeś królem areny! Dziękujemy za grę w Miecze i Kalosze!")
		break