class Ksiazka:
    def __init__(self, tytul, autor, rok, isbn):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.isbn = isbn

    def __str__(self):
        """Ładny opis książki"""
        return f"'{self.tytul}' autor: {self.autor}, rok: {self.rok}, ISBN: {self.isbn}"

    def __repr__(self):
        """Techniczny opis"""
        return f"Ksiazka('{self.tytul}', '{self.autor}', {self.rok}, '{self.isbn}')"

    def __eq__(self, other):
        """Dwie książki są równe jeśli mają ten sam ISBN"""
        if not isinstance(other, Ksiazka):
            return False
        return self.isbn == other.isbn


class Biblioteka:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.ksiazki = []

    def dodaj(self, ksiazka):
        if ksiazka in self.ksiazki:
            print(f"Książka o ISBN {ksiazka.isbn} już istnieje.")
        else:
            self.ksiazki.append(ksiazka)
            print(f"Dodano: {ksiazka.tytul}")

    def usun(self, isbn):
        for k in self.ksiazki:
            if k.isbn == isbn:
                self.ksiazki.remove(k)
                print(f"Usunięto: {k.tytul}")
                return
        print(f"Nie znaleziono książki o ISBN {isbn}.")

    def szukaj(self, fraza):
        fraza = fraza.lower()
        znalezione = [k for k in self.ksiazki if fraza in k.tytul.lower() or fraza in k.autor.lower()]
        return znalezione

    def __len__(self):
        return len(self.ksiazki)

    def __str__(self):
        return f"Biblioteka '{self.nazwa}' ma {len(self.ksiazki)} książek."


# ===== TEST =====
bib = Biblioteka("Moja Biblioteka")
bib.dodaj(Ksiazka("Władca Pierścieni", "Tolkien", 1954, "978-0-123"))
bib.dodaj(Ksiazka("Hobbit", "Tolkien", 1937, "978-0-456"))

print(len(bib))                     # 2
print(bib.szukaj("Tolkien"))        # lista obu książek

print(bib)                          # podsumowanie biblioteki

bib.usun("978-0-123")               # usuwa Władcę Pierścieni
print(len(bib))                     # 1