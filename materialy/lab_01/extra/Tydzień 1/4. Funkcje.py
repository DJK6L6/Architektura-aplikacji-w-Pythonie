import re

def policz_slowa(tekst):
    """Zwraca liczbę słów w tekście."""
    slowa = re.findall(r'\b\w+\b', tekst.lower())
    return len(slowa)

def najdluzsze_slowo(tekst):
    """Zwraca najdłuższe słowo w tekście."""
    slowa = re.findall(r'\b\w+\b', tekst)
    if not slowa:
        return ""
    return max(slowa, key=len)

def czestotliwosc_slow(tekst):
    """Zwraca słownik {słowo: liczba_wystąpień}."""
    slowa = re.findall(r'\b\w+\b', tekst.lower())
    freq = {}
    for s in slowa:
        freq[s] = freq.get(s, 0) + 1
    return freq

def cenzura(tekst, zakazane_slowa):
    """Zamienia zakazane słowa na '***'."""
    def zamien(match):
        slowo = match.group()
        if slowo.lower() in zakazane_slowa:
            return "***"
        return slowo

    return re.sub(r'\b\w+\b', zamien, tekst)


# ===== TEST =====
tekst = """
Python to popularny język programowania. Python jest prosty i potężny.
Programowanie w Pythonie jest przyjemne.
"""

zakazane = ["python"]

print("Liczba słów:", policz_slowa(tekst))
print("Najdłuższe słowo:", najdluzsze_slowo(tekst))
print("Częstotliwość słów:", czestotliwosc_slow(tekst))
print("Po cenzurze:\n", cenzura(tekst, zakazane))