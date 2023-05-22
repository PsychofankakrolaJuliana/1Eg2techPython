# Zad.3
# suma=0
# for i in range(100,1000,2):
#   suma=suma+i
# print(suma)

# Zad.4
# ilosc=0
# for i in range(10,100):
#   if i%2==0 and i%13==0:
#     ilosc=ilosc+1
# print(ilosc)

# Zad.5
# suma=0
# n=int(input("Podaj liczbe: "))
# for i in range(1,n+1):
#   if n%i==0:
#     suma=suma+i
# print(suma)

# Zad.6
# suma=0
# n=int(input("Podaj liczbe: "))
# for i in range(1,n):
#   if n%i==0:
#     suma=suma+i
# if suma>n:
#   print("Liczba jest dzielniko ujemna.")
# else:
#   print("Liczba nie jest dzielniko ujemna.")

# Zad.7
# a=int(input("Podaj licznik: "))
# b=int(input("Podaj minownik: "))
# c=int(input("Podaj licznik: "))
# d=int(input("Podaj mianownik: "))
# if(b!=d):
#   c=c*b
#   d=d*b
#   a=a*d
#   b=b*d
# a=a+c
# from math import gcd
# x=gcd(a,b)
# if x!=0:
#   a=a//x
#   b=b//x
# print(f"{a}/{b}")

# Zad.8
# n=input("Napisz napis: ")
# T=list(n)
# x=0
# ilosc=0
# for i in range(len(T)):
#   x=ord(T[i])
#   if x%2==0:
#     ilosc=ilosc+1
# print(ilosc)

# Zad.9
# ilosc=0
# a=input("Napisz napis: ")
# b=input("Napisz napis: ")
# c=input("Napisz napis: ")
# for i in a:
#   ilosc=ilosc+1
# for i in b:
#   ilosc=ilosc+1
# for i in c:
#   ilosc=ilosc+1
# if ilosc>20:
#   print("TAK")
# else:
#   print("NIE")
