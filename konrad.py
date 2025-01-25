import turtle
"""
Program symuluje ruch "Mrówki Langtona" przy użyciu biblioteki turtle. Mrówka porusza się ( po nieskończonej planszy), wykonując:

Zmienia kolor aktualnej komórki (biały na czarny lub czarny na biały).
Skręca w prawo na białej komórce lub w lewo na czarnej komórce.
Przesuwa się o krok w aktualnym kierunku.

Funkcja:

Użytkownik wpisuje ilość ruchów oraz rozmiar planszy(która zostanie rozszerzona)

Dostosowuje rozmiar ekranu, kształt,rozmiar i szybkość mrówki. Tworzy "plansze" oraz pozycjonuje mrówkę i nadaje jej kierunek.

ruch()- odpowida za ruch mrówki:
Sprawdza kolor aktualnej komórki:

Jeśli komórka jest biała (lub jej brak w słowniku plansza), zmienia jej kolor na czarny, rysuje ślad, i skręca w prawo.
Jeśli komórka jest czarna, zmienia jej kolor na biały, rysuje ślad, i skręca w lewo.
Aktualizuje współrzędne x, y (wykonuje ruch) w zależności od kierunku ruchu.

Zmiana kierunku odbywa się poprzez zmiane wartości w zmiennej "kierunek"
"""

def ruch():
    max_x = int(input("Podaj szerokość planszy:")) * 10
    if (max_x < 0 ):
        print("Błąd, podaj liczbe naturalna")
        return 0
    max_y = int(input("Podaj wysokość planszy:")) * 10
    if (max_y < 0):
        print("Błąd, podaj liczbe naturalna")
        return 0
    turtle.Screen().bgcolor('white')
    turtle.Screen().screensize(1000, 1000)
    turtle.shape('square')
    turtle.shapesize(0.5)
    turtle.speed(10000000000)
    plansza = {}  # słownik który jako klucze przechowuje komórke a jako wartosc kolor
    ile = int(input("Podaj ilosc ruchów (0 dla nieskończonej liczby ruchów):"))
    if(ile<0):
        print("Błąd, podaj liczbe naturalna")
        return 0
    if ile == 0:
        ile = -1
    x=0
    y=0

    x_ujemny=-max_x/2
    x_dodatni=max_x/2
    y_ujemny=-max_y/2
    y_dodatni=max_y/2

    def rozszerz():
        nonlocal x, y,x_dodatni, y_dodatni , x_ujemny, y_ujemny
        if x < x_ujemny:
            x_ujemny = x_ujemny-10
        elif x > x_dodatni:
            x_dodatni = x_dodatni+10
        if y < y_ujemny:
            y_ujemny = y_ujemny-10
        elif y > y_dodatni:
            y_dodatni = y_dodatni+10

    kierunek = 0  # 0 = gora, 1 = prawo, 2 = doł, 3 = lewo
    while ile>0 or ile==-1:
        rozszerz()
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

        if (ile != -1):
            ile = ile - 1

        if ile==1:
            r_x=x_dodatni-x_ujemny
            r_y=y_dodatni-y_ujemny
            if(r_x<=max_x):
                r_x=r_x-10
            if (r_y <= max_y):
                r_y = r_y - 10

            print("rozmiazy rosrzeżonej planszy to:", 1+(r_x)/10, "x", 1+(r_y)/10)
ruch()
