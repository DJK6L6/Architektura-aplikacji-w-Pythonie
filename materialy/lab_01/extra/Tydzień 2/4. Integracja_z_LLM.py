import requests
import json

API_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

historia = []

print("Rozmawiaj z AI. Wpisz 'quit', aby zakończyć.")

while True:
    user_input = input("Ty: ")
    if user_input.lower() == "quit":
        break

    # dodajemy wiadomość użytkownika do historii
    historia.append({"role": "user", "content": user_input})

    prompt = ""
    for msg in historia:
        role = msg["role"]
        content = msg["content"]
        prompt += f"{role}: {content}\n"
    prompt += "assistant:"

    try:
        response = requests.post(API_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        })
        data = response.json()
        odpowiedz = data.get("response", "[Brak odpowiedzi]")
    except Exception as e:
        odpowiedz = f"Błąd w komunikacji z API: {e}"

    # dodajemy odpowiedź AI do historii
    historia.append({"role": "assistant", "content": odpowiedz})

    print(f"AI: {odpowiedz}")

# zapis historii do pliku JSON
plik_historia = "materialy/lab_01/extra/json/historia_ollama.json"
with open(plik_historia, "w", encoding="utf-8") as f:
    json.dump(historia, f, ensure_ascii=False, indent=2)

print(f"Historia rozmowy zapisana w pliku: {plik_historia}")