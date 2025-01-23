"""
Działanie funkcji -mrówka chodzi po planszy, w zależności od koloru skręca w prawo lub w lewo i zostawia na
odwiedzonym polu kolor przeciwny do tego na którym stanął.

zmienne
import turtle – Biblioteka do tworzenia rysunków i grafik
plansza = turtle.Screen() - tworzy plansze po której będzie poruszać się mrówka
pola = {} - tworzy słownik który przechowuje kolory pól
ant = turtle.Turtle() - tworzy mrówke
ant.shape('square') - ksztłt mrówki
ant.shapesize(0.5) - rozmiar kształtu mrówki
ant.speed(0) - prędkośc mrówki (im mniejsza wartość tym szybciej sie przemieszcza)
position = (int(ant.xcor()), int(ant.ycor())) - zwraca współrzędne mrówki

"""

import turtle

def langton():

    plansza = turtle.Screen()

    pola = {}

    ant = turtle.Turtle()
    ant.shape('square')
    ant.shapesize(0.5)
    ant.speed(0)

    step = 10

    while True:
        position = (int(ant.xcor()), int(ant.ycor()))

        if position not in pola or pola[position] == "white":
            ant.fillcolor("black")
            ant.stamp()
            pola[position] = "black"
            ant.right(90)
        else:
            ant.fillcolor("white")
            ant.stamp()
            pola[position] = "white"
            ant.left(90)

        ant.forward(step)

langton()
