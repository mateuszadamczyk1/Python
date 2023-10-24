import math

h = int(input("What is the height of the wall? "))
w = int(input("What is the width of the wall? "))
c = int(input("What is the coverage of the paint? "))


def coverage(h, w, c):
    number = (h * w)/c
    number = math.ceil(number)
    print(number)

coverage(h, w, c)    