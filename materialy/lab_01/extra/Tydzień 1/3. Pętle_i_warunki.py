import random

while True:
    liczba = random.randint(1, 100)
    proby = 0

    print("Zgadnij liczbę od 1 do 100!")

    while True:
        guess = int(input("Podaj swoją liczbę: "))
        proby += 1

        if guess < liczba:
            print("Za mało!")
        elif guess > liczba:
            print("Za dużo!")
        else:
            print(f"Brawo! Zgadłeś w {proby} próbach 🎉")
            break

    # Pytanie o ponowną grę
    again = input("Czy chcesz zagrać ponownie? (t/n): ").lower()
    if again != 't':
        print("Dzięki za grę!")
        break