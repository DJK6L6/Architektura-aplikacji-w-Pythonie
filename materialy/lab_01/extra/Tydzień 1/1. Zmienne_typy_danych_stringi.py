dane = input("Podaj imię i nazwisko: ")

imie, nazwisko = dane.split()

# 1. Inicjały wielkimi literami
inicjaly = imie[0].upper() + "." + nazwisko[0].upper() + "."
print("Inicjały:", inicjaly)

# 2. Imię od tyłu
imie_od_tylu = imie[::-1]
print("Imię od tyłu:", imie_od_tylu)

# 3. Liczba liter (bez spacji)
liczba_liter = len(imie + nazwisko)
print("Liczba liter (bez spacji):", liczba_liter)