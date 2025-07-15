produkty = []  # lista słowników

def dodaj_produkt(): # funkcje
    produkt = {}
    produkt["nazwa"] = input("Podaj nazwę produktu: ")
    produkt["cena"] = float(input("Podaj cenę produktu: "))
    produkt["ilość"] = int(input("Podaj ilość produktu: "))
    produkty.append(produkt)
    print(" Dodano produkt.")

def pokaz_produkty():
    if not produkty:
        print(" Lista produktów jest pusta.")
    else:
        print("\n Lista produktów:")
        for i, p in enumerate(produkty, start=1):
            print(f"{i}. {p['nazwa']} | Cena: {p['cena']} zł | Ilość: {p['ilość']} szt.")

def edytuj_produkt():
    pokaz_produkty()
    index = int(input("Podaj numer produktu do edycji: ")) - 1
    if 0 <= index < len(produkty):
        produkty[index]["nazwa"] = input("Nowa nazwa produktu: ")
        produkty[index]["cena"] = float(input("Nowa cena: "))
        produkty[index]["ilość"] = int(input("Nowa ilość: "))
        print(" Produkt zaktualizowany.")
    else:
        print(" Nieprawidłowy numer.")

def usun_produkt():
    pokaz_produkty()
    index = int(input("Podaj numer produktu do usunięcia: ")) - 1
    if 0 <= index < len(produkty):
        usuniety = produkty.pop(index)
        print(f" Usunięto produkt: {usuniety['nazwa']}")
    else:
        print(" Nieprawidłowy numer.")

def zapisz_do_pliku():
    with open("produkty.txt", "w", encoding="utf-8") as plik:
        for p in produkty:
            plik.write(f"{p['nazwa']}, {p['cena']} zł, {p['ilość']} szt.\n")
    print(" Lista produktów zapisana do pliku 'produkty.txt'.")

# MENU GŁÓWNE
while True:
    print("\n=== MENU ===")
    print("1. Dodaj produkt")
    print("2. Pokaż produkty")
    print("3. Edytuj produkt")
    print("4. Usuń produkt")
    print("5. Zapisz do pliku")
    print("6. Zakończ")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        dodaj_produkt()
    elif wybor == "2":
        pokaz_produkty()
    elif wybor == "3":
        edytuj_produkt()
    elif wybor == "4":
        usun_produkt()
    elif wybor == "5":
        zapisz_do_pliku()
    elif wybor == "6":
        print(" Kończę program...")
        break
    else:
        print(" Nieznana opcja.")
