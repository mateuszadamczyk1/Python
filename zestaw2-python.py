#Zadanie 1 - prosty kalkulator
def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        return "Dzielenie przez 0 jest niedozwolone."
    return a / b

while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")
    
    choice = input("Podaj numer operacji (1/2/3/4/5): ")
    
    if choice == '5':
        break
    
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    
    if choice == '1':
        print("Wynik: ", dodawanie(num1, num2))
    elif choice == '2':
        print("Wynik: ", odejmowanie(num1, num2))
    elif choice == '3':
        print("Wynik: ", mnozenie(num1, num2))
    elif choice == '4':
        print("Wynik: ", dzielenie(num1, num2))
    else:
        print("Niepoprawny wybór operacji.")


#Zadanie 2 - obliczanie sumy, średniej i mediany wpisanych liczb
import statistics

numbers = input("Podaj liczby oddzielone spacjami: ").split()
numbers = [int(num) for num in numbers]

suma = sum(numbers)
srednia = statistics.mean(numbers)
mediana = statistics.median(numbers)

print(f"Suma: {suma}")
print(f"Średnia: {srednia}")
print(f"Mediana: {mediana}")


#Zadanie 3 - szyfr cezara
def cezar(tekst, przesuniecie):
    zaszyfrowany = ""
    for litera in tekst:
        if litera.isalpha():
            if litera.islower():
                zaszyfrowany += chr(((ord(litera) - ord('a') + przesuniecie) % 26) + ord('a'))
            else:
                zaszyfrowany += chr(((ord(litera) - ord('A') + przesuniecie) % 26) + ord('A'))
        else:
            zaszyfrowany += litera
    return zaszyfrowany

tekst = input("Podaj tekst do zaszyfrowania/dezaszyfrowania: ")
przesuniecie = int(input("Podaj przesunięcie: "))
zaszyfrowany_tekst = cezar(tekst, przesuniecie)
print("Zaszyfrowany/dezaszyfrowany tekst: ", zaszyfrowany_tekst)


#Zadanie 4 - palindrom
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

word = input("Podaj słowo: ")
if is_palindrome(word):
    print("To jest palindrom.")
else:
    print("To nie jest palindrom.")


#Zadanie 5 - ilość spacji
with open('plik.txt', 'r') as file:
    text = file.read()
    spaces_count = text.count(' ')

with open('wynik.txt', 'w') as result_file:
    result_file.write(f"Liczba spacji: {spaces_count}")


#Zadanie 6 - klasa kolo, obwod i pole kola
import math

class Kolo:
    def __init__(self, promien):
        self.promien = promien

    def obwod(self):
        return 2 * math.pi * self.promien

    def pole(self):
        return math.pi * self.promien ** 2

kolo = Kolo(5)
print(f"Obwód koła: {kolo.obwod()}")
print(f"Pole koła: {kolo.pole()}")


#Zadanie 7 - odleglosc miedzy dwoma punktami
import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def odleglosc(self, inny_punkt):
        return math.sqrt((self.x - inny_punkt.x)**2 + (self.y - inny_punkt.y)**2)

punkt1 = Punkt(1, 2)
punkt2 = Punkt(4, 6)
odleglosc = punkt1.odleglosc(punkt2)
print(f"Odległość pomiędzy punktami: {odleglosc}")


#Zadanie 8 - klasa odwracajaca ciag znakow po wyrazie
class CiagZnakow:
    def odwroc_po_wyrazie(self, tekst):
        slowa = tekst.split()
        odwrocone_slowa = [slowo[::-1] for slowo in slowa]
        return ' '.join(odwrocone_slowa)

ciag = CiagZnakow()
tekst = "Jestem Groot. Jestem Groot."
odwrocony_tekst = ciag.odwroc_po_wyrazie(tekst)
print(odwrocony_tekst)
