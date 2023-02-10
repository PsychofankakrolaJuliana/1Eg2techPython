# Zad.1
# x  = int(input("Podaj liczbę: "))
# suma=0
# while x>0:
#   suma=suma+x%10
#   x=x//10
# print(suma)

# # Zad.2
# n = int(input("Podaj liczbe: "))
# for i in range(2,n):
#   if n%i==0:
#     print("Podana liczba nie jest pierwsza")
#   else:
#     print("Podana liczba nie jest pierwsza")

# Zad.3
# n = int(input("Podaj liczbe: "))
# suma=0
# for i in range(1,n):
#   if n%i==0:
#     suma=suma+i
# if suma==n:
#   print("Liczba jest doskonała")
# else:
#   print("Nie jest doskonała ta liczba")

# Zad.4
# a = int(input("Podaj liczbę: "))
# b = int(input("Podaj drugą liczbe: "))
# while a!=b:
#   if a>b: a=a-b
#   elif b>a: b=b-a
# if a==1:
#   print("Podane liczby są względnie pierwsze")
# else:
#   print("Podane liczby nie są względnie pierwsze")

# Zad.5
# m = int(input("Podaj liczbe: "))
# for i in range(10,20):
#   x=m
#   y=i
#   while y >0:
#     x,y=y, x%y
#   nwd = x
#   if x==1:
#     print(i, end=" ")

# Zad.6
# a = int(input("Podaj liczbę: "))
# b = int(input("Podaj drugą liczbe: "))
# x=a
# y=b
# while y>0:
#   if a>b: a=a-b
#   elif b>a: b=b-a
# c=a//x
# d=b//x
# print(f"{a}/{b}={c}/{d}")

# Zad.7
# from math import gcd
# l=int(input("Podaj licznik: "))
# m=int(input("Podaj mianownik: "))
# x=l//m
# l=l%m
# d=gcd(l,m)
# l=l//d
# m=m//d
# print(f"{x} {l}/{m}")

# Zad.8
# for i in range(2,10000):
#   suma=0
#   for j in range(1,i):
#     if i%j==0:
#       suma1 +=j
#   suma2=0
#   for k in range(1,suma1):
#     if suma1%k==0:
#       suma2+=k
#   if suma1 == suma2:
#     print(f"({suma 1},{suma2})")

# Zad.9
# def czy_pierwsza(n):
#   for i in range(2,n):
#     if n%i==0:
#       return False
#   return True
# for i in range(10,100):
#   for j in range(2,i):
#     if i%j==0:
#       if czy_pierwsza(j) and czy_pierwsza(i//j):
#         print(i, end=" ")
#         break 

# Zad.10
# n = int(input("Podaj liczbę: "))
# for i in range(2,n):
#   if n%i==0:
#     print("Liczba nie jest pierwsza")
#     break
# else:
#   a=n+2
#   for i in range(2,a):
#     if a%i==0:
#       print("Liczba nie jest pierwsza")
#       break
#   else:
#     print("Podane liczby som bliźniacze")