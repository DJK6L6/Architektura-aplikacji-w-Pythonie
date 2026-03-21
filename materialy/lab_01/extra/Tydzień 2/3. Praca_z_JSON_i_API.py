import requests
import json
import os

HISTORIA_FILE = "materialy/lab_01/extra/json/historia_pogody.json"

# ===== Funkcja pobierająca pogodę =====
def pobierz_pogode(miasto, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={miasto}&appid={api_key}&units=metric&lang=pl"
    response = requests.get(url)
    
    if response.status_code == 200:
        dane = response.json()
        wynik = {
            "miasto": dane["name"],
            "temperatura": dane["main"]["temp"],
            "opis": dane["weather"][0]["description"],
            "wilgotnosc": dane["main"]["humidity"]
        }
        return wynik
    else:
        print("Nie udało się pobrać pogody. Sprawdź nazwę miasta.")
        print(response.text)
        return None

# ===== Funkcja zapisująca historię =====
def zapisz_historie(pogoda):
    historia = []
    if os.path.exists(HISTORIA_FILE):
        with open(HISTORIA_FILE, "r", encoding="utf-8") as f:
            historia = json.load(f)
    historia.append(pogoda)
    with open(HISTORIA_FILE, "w", encoding="utf-8") as f:
        json.dump(historia, f, ensure_ascii=False, indent=2)

# ===== Główna pętla =====
def main():
    api_key = input("Podaj swój API key z OpenWeatherMap: ").strip()
    
    while True:
        miasto = input("\nPodaj miasto (lub 'koniec' aby wyjść): ").strip()
        if miasto.lower() == "koniec":
            print("Koniec programu.")
            break
        
        pogoda = pobierz_pogode(miasto, api_key)
        if pogoda:
            print(f"\nPogoda w {pogoda['miasto']}:")
            print(f"Temperatura: {pogoda['temperatura']} °C")
            print(f"Opis: {pogoda['opis']}")
            print(f"Wilgotność: {pogoda['wilgotnosc']}%")
            
            zapisz_historie(pogoda)

if __name__ == "__main__":
    main()