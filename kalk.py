import math
#  import sys
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
#filename="kalkfile.log"


def pole_prostokata(a, b):
    return a * b


def pole_kwadratu(a):
    return a * a


def pole_rombu(a, b, h):
     return (a + b) / 2 * h


def pole_koła(r):
    return math.pi * r** 2


def pole_trójkata(a, h):
    return 0.5 * a * h


#  wybór = (input("1 - Pole prostokąta, 2 - Pole kwadratu, 3 - Pole rombu, 4 - Pole pizzy, 5 - Pole trójkąta: "))


definicje = {}

while (True):

    print("1: Pole prostokąta")
    print("2: Pole kwadratu")
    print("3: Pole rombu")
    print("4: Pole pizzy")
    print("5: Pole trójąta")
    print("6: Zakończ")

    wybór = input("Co chcesz zrobić? ")

    if (wybór == '1'):
        a = int(input("Wprowadż długość boku a: "))
        b = int(input("Wprowadż długość boku b: "))
        print(pole_prostokata(a, b))
    elif (wybór == '2'):
        a = int(input("Wprowadż długość boku a: "))
        print(pole_kwadratu(a))
    elif (wybór == '3'):
        a = int(input("Wprowadż długość boku a: "))
        b = int(input("Wprowadż długość boku b: "))
        h = int(input("Wprowadż wysokość h: "))
        print(pole_rombu(a, b, h))
    elif (wybór == '4'):
        r = int(input("Wprowadż promień koła r: "))
        print(pole_koła(r))

    elif (wybór == '5'):
        a = int(input("Wprowadż długość boku a: "))
        h = int(input("Wprowadż wysokość h: "))
        print(pole_trójkata(a, h))

    elif ( wybór > '5'):
        print("ucha, ucha, taniec brzucha")
        break
    else:
        print(" HE, He, he, tra la la - ten znak to nie jest liczba!! ")
        break



