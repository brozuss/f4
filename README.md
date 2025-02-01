# Mrówka Langtona 
## Opis Projektu 
- Ten program to implementacja symulacji mrówki Langtona w języku Python. Mrówka Langtona to dwu-wymiarowa maszyna Turinga, której proste zasady prowadzą do zaskakująco złożonego zachowania. Symulacja pozwala na wizualizację ruchu mrówki po siatce oraz oferuje interaktywną obsługę za pomocą przycisków.

## Funkcje programu:
- Personalizacja mrówki i planszy:
  - Możliwość wyboru koloru mrówki.
  - Określenie prędkości wykonywania ruchów przez mrówkę.
  - Ustawienie rozmiaru planszy.

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
    - Jeśli mrówka przekroczy granicę mapy, pojawi się po drugiej stronie osi.

## Instalacja:
1. Pobieranie:
   - pobierz repozytorium (https://github.com/brozuss/f4/archive/refs/heads/main.zip)
   - rozpakuj plik main.zip
2. Stwórz środowisko - otwórz CMD (wiersz poleceń)
    - Przejdź do katalogu "\f4-main"
    - "pip install virtualenv"
    - "python -m venv venv"
    - Uruchom środowisko wirtualne:
      - UNIX - "source venv/scripts/activate" 
      - WINDOWS - "venv\Scripts\activate.bat"
3. Zainstaluj biblioteki (cofnij się do \f4-main:
   - "pip install -r requirements.txt"

## Uruchomienie programu i obsługa:
1. Uruchomienie:
    - "python main.py"
   
2. Uruchomienie z parametrami:
    - "python --color ~KOLOR~ -size ~ROZMIAR~ --speed ~PRĘDKOŚĆ~"
    - "-KOLOR-" - kolor mrówki (domyślnie: fioletowy).
    - "-ROZMIAR-" - rozmiar planszy (domyślnie 600x600)
    - "-PRĘDKOŚĆ-" - prędkość poruszania sie mrówki (domyślnie 0.01, - ilość sekund na krok)
      
   2.1 Przykłady użycia:
     python main.py --color red --step 20 --cells 50
     python main.py --color red --size 600x600
3. Obsługa:
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
