import turtle
import random

t = turtle.Turtle()

vridning = int(input("Walla vilken vridning? Skriv här brur:"))


def rita_kvadrat(sida):
    for i in range(4):
        t.forward(sida)
        t.right(90)
  

def rita_triangel(sida):
    for i in range(3):
        t.forward(sida)
        t.right(120)

def rita_cirkel(radie):
    t.circle(radie)

def kvadrat_figur(antal, fart, sida, förskjutning):
    
    for i in range(antal):
        t.color(random.random(), random.random(), random.random())
        t.speed(fart)
        rita_triangel(sida)
        t.penup()
        t.right(vridning)
        t.forward(förskjutning)
        t.pendown()


kvadrat_figur(500,50000,100,1)


turtle.done()