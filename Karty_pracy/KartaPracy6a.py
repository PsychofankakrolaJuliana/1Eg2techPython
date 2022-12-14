# Zad.1
# x  = int(input("Podaj liczbę: "))
# suma=0
# while x>0:
#   suma=suma+x%10
#   x=x//10
# print(suma)
# Zad.2
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
# for i in range(10,19):
#   x=m
#   y=i
#   while y >0:
#     x,y=y, x%y
#   nwd = x
#   print(f"Mamy parke : {m}, {i}")
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
a = int(input("Podaj licznik: "))
b = int(input("Podaj mianownik: "))
c=a
d=b
while c>0:
if c>d: c=c-d
elif d>c: d=d-c
x=a/c
y=b/c
