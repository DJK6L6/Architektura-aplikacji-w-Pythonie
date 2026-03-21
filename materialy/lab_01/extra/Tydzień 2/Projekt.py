import requests
import json

class Asystent:
    def __init__(self, imie, specjalizacja, model="llama3.2", api_url="http://localhost:11434/api/generate"):
        self.imie = imie
        self.specjalizacja = specjalizacja
        self.model = model
        self.api_url = api_url
        self.historia = []

    def zapytaj(self, pytanie):
        """Wysyła pytanie do lokalnego Ollama, zwraca odpowiedź i aktualizuje historię"""
        self.historia.append({"role": "user", "content": pytanie})

        # Tworzymy prompt z całą historią + instrukcja systemowa
        prompt = f"system: {self.specjalizacja}\n"
        for msg in self.historia:
            prompt += f"{msg['role']}: {msg['content']}\n"
        prompt += "assistant:"

        try:
            response = requests.post(self.api_url, json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            })
            data = response.json()
            odpowiedz = data.get("response", "[Brak odpowiedzi]")
        except Exception as e:
            odpowiedz = f"Błąd w komunikacji z Ollama: {e}"

        self.historia.append({"role": "assistant", "content": odpowiedz})
        return odpowiedz

    def zapisz_historie(self, plik):
        """Zapisuje historię rozmowy do pliku JSON"""
        with open(plik, "w", encoding="utf-8") as f:
            json.dump(self.historia, f, ensure_ascii=False, indent=2)
        print(f"Historia zapisana w pliku: {plik}")

    def wczytaj_historie(self, plik):
        """Wczytuje poprzednią rozmowę z pliku JSON"""
        try:
            with open(plik, "r", encoding="utf-8") as f:
                self.historia = json.load(f)
            print(f"Historia wczytana z pliku: {plik}")
        except FileNotFoundError:
            print(f"Plik {plik} nie istnieje.")
        except json.JSONDecodeError:
            print(f"Plik {plik} jest uszkodzony lub niepoprawny JSON.")

    def podsumuj(self):
        """Prosi AI o podsumowanie dotychczasowej rozmowy"""
        if not self.historia:
            return "Brak wiadomości do podsumowania."
        tresc = "\n".join([f"{h['role']}: {h['content']}" for h in self.historia])
        return self.zapytaj(f"Podsumuj proszę następującą rozmowę:\n{tresc}")

    def __str__(self):
        return f"Asystent '{self.imie}' ({self.specjalizacja[:30]}...) — {len(self.historia)} wiadomości"


# ===== Przykład użycia =====
if __name__ == "__main__":
    bot = Asystent(
        imie="PyHelper",
        specjalizacja="Jesteś ekspertem Pythona. Tłumaczysz koncepty prosto i z przykładami kodu."
    )

    while True:
        user_input = input("Ty: ")
        if user_input.lower() == "quit":
            break
        odpowiedz = bot.zapytaj(user_input)
        print(f"AI: {odpowiedz}")

    bot.zapisz_historie("materialy/lab_01/extra/json/historia_ollama.json")