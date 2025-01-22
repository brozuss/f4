import turtle
"""
Program symuluje ruch "Mrówki Langtona" przy użyciu biblioteki turtle. Mrówka porusza się ( po nieskończonej planszy), wykonując:

Zmienia kolor aktualnej komórki (biały na czarny lub czarny na biały).
Skręca w prawo na białej komórce lub w lewo na czarnej komórce.
Przesuwa się o krok w aktualnym kierunku.

Funkcja:

Dostosowuje rozmiar ekranu, kształt,rozmiar i szybkość mrówki. Tworzy "plansze" oraz pozycjonuje mrówkę i nadaje jej kierunek.

ruch()- odpowida za ruch mrówki:
Sprawdza kolor aktualnej komórki:

Jeśli komórka jest biała (lub jej brak w słowniku plansza), zmienia jej kolor na czarny, rysuje ślad, i skręca w prawo.
Jeśli komórka jest czarna, zmienia jej kolor na biały, rysuje ślad, i skręca w lewo.
Aktualizuje współrzędne x, y (wykonuje ruch) w zależności od kierunku ruchu.

Zmiana kierunku odbywa się poprzez zmiane wartości w zmiennej "kierunek"
"""

def ruch():
    turtle.Screen().bgcolor('white')
    turtle.Screen().screensize(1000, 1000)
    turtle.shape('square')
    turtle.shapesize(0.5)
    turtle.speed(10000)
    plansza = {}  # słownik który jako klucze przechowuje komórke a jako wartosc kolor

    x=0
    y=0
    kierunek = 0  # 0 = gora, 1 = prawo, 2 = doł, 3 = lewo
    #pętla działa bez końca bez zadanej liczbie kroków i rozmiaru planszy, zostanie zmienione w pozniejszej wersji (moze)
    while True:
        kroki = 10

        if  (x, y) not in plansza or plansza[(x, y)] == "white":
            turtle.fillcolor("black")
            turtle.goto(x, y)
            turtle.stamp()
            plansza[(x, y)] = "black"

            # skręt w prawo
            kierunek = (kierunek + 1) % 4

        elif plansza[(x, y)] == "black":
            turtle.fillcolor("white")
            turtle.goto(x, y)
            turtle.stamp()
            plansza[(x, y)] = "white"

            # skręt w lewo
            kierunek =(kierunek - 1) % 4


        if kierunek == 0:
            y = y+ kroki
        elif kierunek == 1:
            x = x+ kroki
        elif kierunek == 2:
            y = y- kroki
        elif kierunek == 3:
            x = x- kroki

ruch()
