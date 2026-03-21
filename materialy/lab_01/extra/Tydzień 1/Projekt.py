import csv
import os

kontakty = []

# ===== FUNKCJE =====

def dodaj_kontakt():
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    
    telefon = input("Telefon: ")
    if not telefon.isdigit():
        print("Błąd: telefon musi zawierać tylko cyfry!")
        return
    
    email = input("Email: ")
    if "@" not in email:
        print("Błąd: niepoprawny email!")
        return

    kontakt = {
        "imie": imie,
        "nazwisko": nazwisko,
        "telefon": telefon,
        "email": email
    }
    
    kontakty.append(kontakt)
    print("Kontakt dodany!")

def wyswietl_kontakty():
    if not kontakty:
        print("Brak kontaktów.")
        return
    
    for i, k in enumerate(kontakty, 1):
        print(f"{i}. {k['imie']} {k['nazwisko']} | tel: {k['telefon']} | email: {k['email']}")

def wyszukaj_kontakt():
    szukaj = input("Podaj imię lub nazwisko: ").lower()
    znalezione = [k for k in kontakty if szukaj in k["imie"].lower() or szukaj in k["nazwisko"].lower()]
    
    if znalezione:
        for k in znalezione:
            print(f"{k['imie']} {k['nazwisko']} | {k['telefon']} | {k['email']}")
    else:
        print("Nie znaleziono kontaktu.")

def usun_kontakt():
    wyswietl_kontakty()
    try:
        indeks = int(input("Podaj numer kontaktu do usunięcia: "))
        if 1 <= indeks <= len(kontakty):
            usuniety = kontakty.pop(indeks - 1)
            print(f"Usunięto: {usuniety['imie']} {usuniety['nazwisko']}")
        else:
            print("Nieprawidłowy numer.")
    except ValueError:
        print("Podaj liczbę!")

def zapisz_do_csv():
    os.makedirs("csv", exist_ok=True)
    
    sciezka = os.path.join("csv", "kontakty.csv")
    
    with open(sciezka, "w", newline="", encoding="utf-8") as plik:
        writer = csv.DictWriter(plik, fieldnames=["imie", "nazwisko", "telefon", "email"])
        writer.writeheader()
        writer.writerows(kontakty)
    
    print("Zapisano do", sciezka)

def wczytaj_z_csv():
    global kontakty
    sciezka = os.path.join("csv", "kontakty.csv")
    
    try:
        with open(sciezka, "r", encoding="utf-8") as plik:
            reader = csv.DictReader(plik)
            kontakty = list(reader)
        print("Wczytano kontakty.")
    except FileNotFoundError:
        print("Plik nie istnieje!")

def menu():
    print("\n--- MENEDŻER KONTAKTÓW ---")
    print("1. Dodaj kontakt")
    print("2. Wyświetl kontakty")
    print("3. Wyszukaj kontakt")
    print("4. Usuń kontakt")
    print("5. Zapisz do CSV")
    print("6. Wczytaj z CSV")
    print("7. Wyjdź")

# ===== GŁÓWNA PĘTLA =====

while True:
    menu()
    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        dodaj_kontakt()
    elif wybor == "2":
        wyswietl_kontakty()
    elif wybor == "3":
        wyszukaj_kontakt()
    elif wybor == "4":
        usun_kontakt()
    elif wybor == "5":
        zapisz_do_csv()
    elif wybor == "6":
        wczytaj_z_csv()
    elif wybor == "7":
        print("Koniec programu.")
        break
    else:
        print("Nieprawidłowy wybór!")