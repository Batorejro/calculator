import math
import time


def pole_prostokata(a, b):
    return a * b


def pole_kwadratu(a):
    return a * a


def pole_rombu(a, b, h):
    return (a + b) / 2 * h


def pole_koła(r):
    return math.pi * r ** 2


def pole_trójkata(a, h):
    return 0.5 * a * h


def finish_timer(start):
    end = time.perf_counter()
    return end-start


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
        start = time.perf_counter()
        a = int(input("Wprowadż długość boku a: "))
        b = int(input("Wprowadż długość boku b: "))   
        print(pole_prostokata(a, b))
        print("Czas operacyjny działania: ", finish_timer(start))
    elif (wybór == '2'):
        start = time.perf_counter()
        a = int(input("Wprowadż długość boku a: "))
        end = time.perf_counter()
        print(pole_kwadratu(a))
        print("Czas operacyjny działania: ", finish_timer(start))
    elif (wybór == '3'):
        start = time.perf_counter()
        a = int(input("Wprowadż długość boku a: "))
        b = int(input("Wprowadż długość boku b: "))
        h = int(input("Wprowadż wysokość h: "))
        print(pole_rombu(a, b, h))
        print("Czas operacyjny działania: ", finish_timer(start))

    elif (wybór == '4'):
        start = time.perf_counter()
        r = int(input("Wprowadż promień koła r: "))
        print(pole_koła(r))
        print("Czas operacyjny działania: ", finish_timer(start))

    elif (wybór == '5'):
        start = time.perf_counter()
        a = int(input("Wprowadż długość boku a: "))
        h = int(input("Wprowadż wysokość h: "))
        print(pole_trójkata(a, h))
        print("Czas operacyjny działania: ", finish_timer(start))

    elif (wybór > '5'):
        print("ucha, ucha, taniec brzucha")
        break
    else:
        print(" HE, He, he, tra la la - ten znak to nie jest liczba!! ")
        break
