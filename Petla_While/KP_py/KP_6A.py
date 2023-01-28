# Petla_While//KP_py//KP_6A.py
# Zad.1
# n=int(input("Podaj liczbe: "))
# suma=0
# while n>0:
#   suma=suma+n%10
#   n=n//10
# print(suma)

# Zad.2
# n=int(input("Podaj liczbe: "))
# i=2
# F=1
# while i<n:
#   if n%i==0:
#     F=0
#   i=i+1
# if F==1:
#   print("Podana liczba jest pierwsza")
# elif F==0:
#   print("Podana liczba nie jest pierwsza")

# Zad.3
# suma=0
# n=int(input("Podaj liczbe: "))
# i=1
# while i<n:
#   if n%i==0:
#     suma=suma+i
#   i=i+1
# if suma==n:
#   print("Podana liczba jest doskonala")
# else:
#   print("Podana liczba nie jest doskonala")

# Zad.4
# a= int(input("Podaj liczbe: "))
# b= int(input("Podaj liczbe: "))
# x=a
# y=b
# while x!=y:
#   if x>y:
#     x=x-y
#   else:
#     y=y-x
# if x==1 or y==1:
#   print("Podane liczby sa wzglednie pierwsze.")
# else:
#   print("Podane liczby nie sa wzglednie pierwsze.")

# Zad.5
# m=int(input("Podaj liczbe: "))
# i=10
# while i<20:
#   x=i
#   y=m
#   while x!=y:
#     if x>y:
#       x=x-y
#     else:
#       y=y-x
#   if x==1 or y==1:
#     print(i, end=" ")
#   i=i+1

# Zad.6
# a=int(input("Podaj licznik: "))
# b=int(input("Podaj licznik: "))
# x=a
# y=b
# while x!=y:
#   if x>y:
#     x=x-y
#   else:
#     y=y-x
# c=a//x
# d=b//y
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

# Zad.8 -> działa w teorii i tylko w teorii
# i=0 
# x=0
# y=0
# suma1=0
# suma2=0
# j=1
# print("Liczby zaprzyjaznione do 10000: ")
# while i<10000:
#   while j<10000:
#     while x<i:
#       x=x+1
#       if i%x==0:
#         suma1+=x
#     while y<j:
#       y=y+1
#       if j%y==0:
#         suma2+=y
#     if suma1==suma2:
#       print(f"{i} i {j}")
#     j=j+1
#   i=i+1