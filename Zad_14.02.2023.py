# Zad_14.0.2023.py
# Zad.1 -> GÓWNO WALONE NIC NIE DZIAŁA
# l1 = int(input("Podaj licznik: "))
# m1 = int(input("Podaj mianownik: "))
# l2 = int(input("Podaj licznik: "))
# m2 = int(input("Podaj mianownik: "))
# l3 = int(input("Podaj licznik: "))
# m3 = int(input("Podaj mianownik: "))
# x = m1
# y = m2
# n = 0
# n = x * y
# while y>0:
#   x=y
#   y=x%y
# n=n//y
# a = m // m1
# b = m // m2
# c = m // m3
# l1 = l1 * a
# m1 = m1 * a
# l2 = l2 * b
# m2 = m2 * b
# l3 = l3 * c
# m3 = m3 * c
# print(f"{l1}/{m1} ; {l2}/{m2} ; {l3}/{m3}")

# Zad.2
suma1=0
suma2=0
for i in range(1,5000):
  for j in range(1,i):
    if i%j==0:
      suma1+=j
  