import csv
import os

# ===== Ścieżki folderów =====
csv_folder = "materialy/lab_01/extra/csv"
raport_folder = "materialy/lab_01/extra/raporty"

sciezka_csv = os.path.join(csv_folder, "studenci.csv")
sciezka_raport = os.path.join(raport_folder, "raport.txt")

# Tworzenie folderów, jeśli nie istnieją
os.makedirs(csv_folder, exist_ok=True)
os.makedirs(raport_folder, exist_ok=True)

# ===== Zmienne do analizy =====
oceny = []
najlepszy_student = None
najwyzsza_ocena = 0

# ===== Odczyt CSV =====
try:
    with open(sciezka_csv, "r", encoding="utf-8") as plik:
        reader = csv.DictReader(plik)
        
        for wiersz in reader:
            try:
                ocena = float(wiersz["ocena"])
            except ValueError:
                print(f"Nieprawidłowa ocena dla {wiersz['imię']} {wiersz['nazwisko']}")
                continue
            
            oceny.append(ocena)
            
            if ocena > najwyzsza_ocena:
                najwyzsza_ocena = ocena
                najlepszy_student = wiersz

    if not oceny:
        print("Brak danych w pliku CSV.")
    else:
        srednia = sum(oceny) / len(oceny)

        # ===== Zapis raportu =====
        with open(sciezka_raport, "w", encoding="utf-8") as plik:
            plik.write(f"Średnia ocen: {srednia:.2f}\n")
            plik.write("Najlepszy student:\n")
            plik.write(f"{najlepszy_student['imię']} {najlepszy_student['nazwisko']} - {najwyzsza_ocena}\n")

        print("Raport zapisany do:", sciezka_raport)

except FileNotFoundError:
    print("Nie znaleziono pliku CSV:", sciezka_csv)
    print("Upewnij się, że plik istnieje w folderze:", csv_folder)