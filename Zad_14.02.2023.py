# Zad_14.0.2023.py
# Zad.1
l1 = int(input("Podaj licznik: "))
m1 = int(input("Podaj mianownik: "))
l2 = int(input("Podaj licznik: "))
m2 = int(input("Podaj mianownik: "))
l3 = int(input("Podaj licznik: "))
m3 = int(input("Podaj mianownik: "))
x = m1
y = m2
n = 0
while x != y:
  n = x * y
while x != y:
  if x > y:
    x = x - y
    n = n / x
  else:
    y = y - x
    n = n / y
z = m3
a = 0
while n != z:
  a = n * z
while n != z:
  if n > z:
    n = n - z
    a = a / n
  else:
    z = z - n
    z = z / a
