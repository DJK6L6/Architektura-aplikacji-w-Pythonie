zakupy = [
    {"nazwa": "mleko", "cena": 4.50, "ilość": 2},
    {"nazwa": "chleb", "cena": 5.00, "ilość": 1},
    {"nazwa": "masło", "cena": 7.99, "ilość": 1},
    {"nazwa": "jajka", "cena": 12.50, "ilość": 1},
    {"nazwa": "mleko", "cena": 4.50, "ilość": 3},
]

# 1. Łączny koszt zakupów
laczny_koszt = sum(produkt["cena"] * produkt["ilość"] for produkt in zakupy)
print("Łączny koszt:", laczny_koszt, "zł")

# 2. Najdroższy produkt (po cenie jednostkowej)
najdrozszy = max(zakupy, key=lambda p: p["cena"])
print("Najdroższy produkt:", najdrozszy["nazwa"], "-", najdrozszy["cena"], "zł")

# 3. Unikalne nazwy produktów
unikalne_produkty = list(set(produkt["nazwa"] for produkt in zakupy))
print("Unikalne produkty:", unikalne_produkty)

# 4. Produkty droższe niż 5 zł
drozsze_niz_5 = [produkt for produkt in zakupy if produkt["cena"] > 5]
print("Produkty droższe niż 5 zł:", drozsze_niz_5)