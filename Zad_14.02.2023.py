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

# Zad.2 -> działa ale mój komputer tego k nie rozumie :)))))))) KOCHAM ŻYCIE
# suma1=0
# suma2=0
# for a in range(1,5000):
#   for x in range(1,a-1):
#     if a%x==0:
#       suma1+=x
#   for b in range(1,5000):
#     for y in range(1,b-1):
#       if b%y==0:
#         suma2+=y
#     if suma1==suma2:
#       print(f"{a} i {b}")

# Zad.3
# ilo=0
# f=1
# for i in range(2,501):
#   for j in range(2,i):
#     if i%j==0:
#       ilo+=1
#       for a in range(2,j):
#         if j%a==0:
#           f=0
#   if ilo==6 and f==1:
#     print(i, end=" ")