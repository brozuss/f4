import turtle
import time

"""

Program tworzy symulację "Mrówki Langtona" za pomocą biblioteki turtle.
Symulacja polega na tym, że mrówka porusza się po siatce (planszy) zgodnie z 3 regułami:
1. Jeżeli znajduje się w komórce żywej, to skręca w prawo o 90 stopni.
2. Jeżeli znajduje się w komórce martwej, to skręca w lewo o 90 stopni.
3. Przechodząc do następnego pola na siatce zmienia jego stan z żywego na martwy lub odwrotnie.

Dzięki bibliotece time możemy operować czasem np. opóźnieniem kroku.

Parametry możemy edytować wedle naszego uznania:
x- Szerokość planszy.
y- Wysokość planszy.
x_0- Położenie początkowe w poziomie.
y_0- Położenie początkowe w pionie.
kroki- Liczba iteracji do wykonania przez mrówkę.
rozmiar_komorki- Rozmiar pojedynczej komórki.
kierunki-  Kierunki ruchu. Odpowiadają za zmiane współrzędnych mrówki (przesunięcie o daną ilość komórek w daną stronę).

Funkcja "rysuj_komorke":
Rysuje pojedynczą komórkę na planszy, przyjmując jako argumenty współrzędne i kolor.

Funkcja "krok":
Symuluje pojedynczy ruch mrówki.
Sprawdza kolor aktualnej komórki.
Zmienia kierunek ruchu w zależności od koloru.
Zmienia kolor komórki.
Aktualizuje pozycję mrówki.

Funkcja "symulacja":
Ustawia siatkę, pozycję mrówki i jej kierunek.
W pętli wykonuje określoną liczbę kroków, wywołując funkcję "krok":
Sprawdza kolor aktualnej komórki.
Jeśli komórka jest biała, to mrówka skręca w lewo, a jeśli jest czarna to skręca w prawo.
Zmienia kolor aktualnej komórki na przeciwny.
Przesuwa mrówkę o jeden krok w nowym kierunku.
Aktualizuje wyświetlany obraz.

Funkcja "rysuj_siatke":
Odpowiada za rysowanie linii siatki na planszy w wybranym kolorze przed rozpoczęciem symulacji.
Linie dzielą planszę na komórki określonej wielkości przez zmienną "rozmiar_komorki".

Wywołanie "symulacja()" odpowiada za wyświetlanie animacji.

"""

# Parametry
x = 100
y = 100
x_0 = 50
y_0 = 50
kroki = 100000
rozmiar_komorki = 10
kierunki = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Rysunek
def rysuj_komorke(x_pozycja, y_pozycja, kolor):
    turtle.penup()
    turtle.goto(x_pozycja, y_pozycja)
    turtle.pendown()
    turtle.fillcolor("black" if kolor else "white")
    turtle.begin_fill()
    for a in range(4):  # Pętla rysująca komórkę
        turtle.forward(1)
        turtle.left(90)
    turtle.end_fill()

# Krok mrówki
def krok(siatka, mrowka_x, mrowka_y, kierunek_mrowki, x, y):  # Wykonuje pojedynczy krok symulacji, zmienia kolor komórki oraz odpowiada za ruch mrówki
    obecna_komorka = siatka[mrowka_y][mrowka_x]
    kierunek_mrowki = (kierunek_mrowki - 1 if obecna_komorka == 0 else kierunek_mrowki + 1) % 4
    siatka[mrowka_y][mrowka_x] = 1 - obecna_komorka
    rysuj_komorke(mrowka_x, mrowka_y, siatka[mrowka_y][mrowka_x])
    dx, dy = kierunki[kierunek_mrowki]
    return siatka, (mrowka_x + dx) % x, (mrowka_y + dy) % y, kierunek_mrowki  # Zwraca zaaktualizowaną siatkę, nową pozycję i nowy kierunek mrówki

# Uruchamianie symulacji
def symulacja():  # Uruchamia symulację
    siatka = [[0] * x for a in range(y)]
    mrowka_x = x_0  # Położenie mrówki w poziomie
    mrowka_y = y_0  # Położenie mrówki w pionie
    kierunek_mrowki = 0
    for a in range(kroki):  # Pętla wykonuje zadaną przez nas ilość iteracji
        siatka, mrowka_x, mrowka_y, kierunek_mrowki = krok(siatka, mrowka_x, mrowka_y, kierunek_mrowki, x, y)
        turtle.update()
        time.sleep(0.01)  # Czas opóźnienia każdej iteracji

# Linie na planszy
def rysuj_siatke(x, y):
    turtle.color("grey")
    turtle.penup()
    for i in range(x + 1):
        turtle.goto(i, 0)
        turtle.pendown()
        turtle.goto(i, y)
        turtle.penup()
    for i in range(y + 1):
        turtle.goto(0, i)
        turtle.pendown()
        turtle.goto(x, i)
        turtle.penup()

turtle.setup(x * rozmiar_komorki, y * rozmiar_komorki)
turtle.setworldcoordinates(0, 0, x, y)
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0, 0)

rysuj_siatke(x, y)  # Rysowanie siatki przed rozpoczęciem symulacji

symulacja()
turtle.done()
