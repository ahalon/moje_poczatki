sklep = []


def dodawanie_produktu():
    produkt = {}
    produkt["nazwa"] = input("Podaj nazwe produktu:")
    while True:
        try:
            produkt["cena"] = float(input("Podaj cene produktu:"))
            break
        except:
            ValueError
            print("Błąd, wpisz poprawną liczbe")
    while True:
        try:
            produkt["ilosc"] = int(input("podaj ilość produktu"))
            break
        except ValueError:
            print("Błąd, wpisz poprawną liczbe")

    sklep.append(produkt)
    print("Dodano produkt")

def pokaz_produkty():
    for i, p in enumerate(sklep, start=1):
        print(f"\n {i}. {p['nazwa']} CENA: {p['cena']} zł ILOŚĆ: {p['ilosc']} szt.")

def najdrozszy_produkt():
    najdrozszy_produkt = None
    najwyzsza_cena = 0
    for produkt in sklep:
        if float(produkt['cena']) > najwyzsza_cena:
            najwyzsza_cena = float(produkt["cena"])
            najdrozszy_produkt = produkt
    print(najdrozszy_produkt)

def najtanszy_produkt():
    najtanszy_produkt = sklep[0]
    najnizsza_cena = int(sklep[0]['cena'])
    for produkt in sklep:
        if float(produkt['cena']) < najnizsza_cena:
            najnizsza_cena = float(produkt['cena'])
            najtanszy_produkt = produkt
    print("\n" , najtanszy_produkt)

def wartosc_sklepu():
    wartosc_sklepu = 0
    for produkt in sklep:
        wartosc_sklepu += float(produkt['cena']) * int(produkt['ilosc'])
    print("\n \n" , wartosc_sklepu, "zł")

def wartosc_over1():
    for i, produkt in enumerate (sklep, start = 1):
        if float(produkt['cena']) > 1:
            print(f" {i}.{produkt['nazwa']}")

def edytuj_produkt():
    pokaz_produkty()
    index = int(input("Podaj numer produktu do edycji: ")) - 1
    if 0 <= index < len(sklep):
        sklep[index]['nazwa'] = input("Podaj nową nazwe:")
        sklep[index]['cena'] = float(input("Podaj nową cene:"))
        sklep[index]['ilosc'] = int(input("Podaj nową ilosc:"))
        print(" Produkt zaktualizowany.")
    else:
        print(" Nieprawidłowy numer.")

def usun_produkt():
    pokaz_produkty()
    index = int(input("Podaj numer do usuniecia:")) - 1
    if 0 <= index < len(sklep):
        usuniety = sklep.pop(index)
        print(f"Usunięto: {usuniety}")
    
def zapisz_dysk():
    with open("sklep.txt", "w", encoding="utf-8") as plik:
        for p in sklep:
            plik.write(f"{p['nazwa']}, {p['cena']} zł, {p['ilosc']} szt.\n")
    print("Zapisano na dysku")

    
while True:
    if not sklep:
        print("Pusta lista produktów!")

    print("\n===MENU===")
    print("1.Dodaj produkt")
    print("2.Pokaż liste")
    print("3.Pokaż najdroższy produkt")
    print("4.Pokaż najtańszy produkt")
    print("5.Pokaż wartość sklepu")
    print("6.Pokaż wszystkie produkty których wartość większa niż 1")
    print("7.Edytuj produkt")
    print("8.Usuń produkt")
    print("9.Zapisz na dysku")
    print("10.Zakończ")


    choice = input("Podaj opcje:")
    
    if choice == "1":
        dodawanie_produktu()
    elif choice == "2":
        pokaz_produkty()
    elif choice == "3":
        najdrozszy_produkt()
    elif choice == "4":
        najtanszy_produkt()
    elif choice == "5":
        wartosc_sklepu()
    elif choice == "6":
        wartosc_over1()
    elif choice == "7":
        edytuj_produkt()
    elif choice == "8":
        usun_produkt()
    elif choice == "9":  
        zapisz_dysk()
    elif choice == "10":
        print("Kończe program...")
        break      
    else:
        print("Nieprawidłowa opcja. Spróbuj ponownie")

    

    


