wiek = input("Podaj wiek uzytkownika: ")
#sprawdzenie czy wiek jest liczba calkowitą
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikację")
wiek=int(wiek)
if wiek<0:
    exit("Wiek nie może być ujemny. Zamykam aplikację")
elif wiek>=0 and wiek<18:
    exit("Jesteś niepełnoletni. Zamykam aplikację")
elif wiek>=18 and wiek<=100:
    print("Witamy w apce. Mozesz kupować u nas energetyki")
elif wiek>=100:
    exit("Jesteś za stary. Zamykam aplikację")
else:
    print("EXCEPTION NOT HANDLED")