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
m = 0
while n != z:
  m = n * z
while n != z:
  if n > z:
    n = n - z
    m = m / n
  else:
    z = z - n
    z = z / m
a = m / m1
b = m / m2
c = m / m3
l1 = l1 * a
m1 = m1 * a
l2 = l2 * b
m2 = m2 * b
l3 = l3 * c
m3 = m3 * c
print(f"{l1}/{m1} ; {l2}/{m2} ; {l3}/{m3}")