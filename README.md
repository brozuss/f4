# Mrówka Langtona 
## Opis Projektu 
- Ten program to implementacja symulacji mrówki Langtona w języku Python. Mrówka Langtona to dwu-wymiarowa maszyna Turinga, której proste zasady prowadzą do zaskakująco złożonego zachowania. Symulacja pozwala na wizualizację ruchu mrówki po siatce oraz oferuje interaktywną obsługę za pomocą przycisków.

## Funkcje programu:
- Personalizacja mrówki i planszy:
- Możliwość wyboru koloru mrówki.
- Określenie wielkości kroku, który wykonuje mrówka.
- Ustawienie liczby komórek planszy.

## Interaktywne GUI:
- Przyciski umożliwiające rozpoczęcie, wstrzymanie i wznowienie symulacji.
- Opcja zapisu aktualnego stanu planszy jako obrazu (langton_grid.png) na pulpicie.

## Zasady symulacji:
- Mrówka Langtona działa według prostych reguł:
    - Jeśli mrówka znajduje się na białym polu:
        - Obraca się w prawo.
        - Zmienia kolor pola na czarny.
    - Jeśli mrówka znajduje się na czarnym polu:
        - Obraca się w lewo.
        - Zmienia kolor pola na biały.
    - Po zmianie koloru pola mrówka porusza się do przodu o określony krok.

## Instalacja:
1. Pobieranie:
   - pobierz repozytorium (https://github.com/brozuss/f4/archive/refs/heads/main.zip)
   - rozpakuj plik main.zip
2. Stwórz środowisko - otwórz CMD (wiersz poleceń)
    - Przejdź do katalogu "\f4"
    - pip install virtualvenv
    - python -m venv venv
    - "source venv/scripts/activate" - Unix
    - "venv/Scripts/activate.bat" - Windows
3. Zainstaluj biblioteki:
   - "pip install -r requirements.txt"

## Uruchomienie programu i obsługa:
1. Uruchomienie:
    - python main.py
        - parametry:
            - "--color" - kolor mrówki (domyślnie: fioletowy).
            - "--step" - rozmiar kroku (domyślnie: 10).
            - "--cells" - liczba komórek planszy w jednej osi (domyślnie: 30).
2. Obsługa:
    - Po uruchomieniu zobaczysz okno GUI z przyciskami:
      - Start - rozpoczęcie symulacji
      - Pause - wstrzymuje symulację
      - Resume - wznawia symulację
      - Save image - zapisuje aktualny stan siatki jako PNG na pulpicie (langton_grid.png)
      
## Autorzy:
- Kacper Brożyński - 287390 (brozuss)
- Mateusz Młot - 287365 (Toja123456)
- Maksymilian Maćkowiak - 287370 (Makovskyyy)
- Konrad Kokot - 287373 (kkondzio)
