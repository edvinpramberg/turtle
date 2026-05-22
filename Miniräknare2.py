operator = input("Välj räknesätt (+, -, *, /): ")

tal1 = float(input("Skriv första talet:"))
tal2 = float(input("Skriv andra talet:"))

def addera(a,b):
    return a + b

def subtrahera(a,b):
    return a-b

def multiplicera(a,b):
    return a*b

def dividera(a,b):
    if b == 0:
        return "Kan inte dividera med 0 din tomte"
    return a/b

while True:

    if operator == "q":
        break

    if operator == "+":
        print(addera(tal1,tal2))

    elif operator == "-":
        print(subtrahera(tal1,tal2))

    elif operator == "*":
        print(multiplicera(tal1,tal2))

    elif operator == "/":
        print(dividera(tal1,tal2))

    operator = input("Välj räknesätt (+, -, *, /) eller q för att avsluta: ")

    if operator != "q":
        tal1 = float(input("Skriv första talet:"))
        tal2 = float(input("Skriv andra talet:"))