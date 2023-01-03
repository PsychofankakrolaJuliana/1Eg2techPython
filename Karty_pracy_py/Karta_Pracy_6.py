# Zad.1
# a = int(input("Podaj liczbe: "))
# b = int(input("Podaj drugom liczbe: "))
# c = int(input("Podaj trzeciom liczbe: "))
# x =c-b
# y=b-a
# d=c/b
# e=b/a
# if(x==y):
#   print("Ciag jest arytmetyczny")
# else:
#   print("Ciąg nie jest arytmetyczny")
# if(d==e):
#   print("Ciag jest geometryczny")
# else:
#   print("Ciag nie jest geometryczny")
# if(a<b<c):
#   print("Ciag jest rosnacy")
# elif(a>b>c):
#   print("Ciag jest malejacy")
# Zad.2
# suma = 0
# for i in range(100,1000):
#   if i%8==0 and i%16!=0:
#     suma=suma+i
# print(suma)
# Zad.3
# x=0
# suma=0
# for i in range(10,99):
#   if i%7==0:
#     x=i
# for j in range(1000,10000):
#   if j%x==0:
#     suma=suma+1
# print(suma)
# Zad.4
# x=0 
# y=0
# suma = 0
# for i in range(10,100):
#   x=i%10
#   y=i%100
#   if y>=x*2:
#     suma=suma+1
# print(suma)
# Zad.5
# suma=0
# sum=0
# x=0
# y=0
# z=0
# for i in range(100,1000):
#   x=i%1000
#   y=i%100
#   z=i%10
#   if x>y+z:
#     suma=suma+i
#     sum=sum+1
# print(f"Suma liczb: {suma}, a ilosc liczb to: {sum}")
# Zad.6
# suma=0
# n = int(input("Podaj ile chcesz liczb: "))
# for i in range(19,100):
#   if i%19==0:
#     suma=suma+i
# print(f"Suam {n} najmniejszych liczb dwucyfrowych podzielnych przez 19 to: {suma}")
# Zad.7
# suma=0
# n = int(input("Podaj liczbe: "))
# for i in range(1000,1000-37*n,-1):
#   if i%37==0:
#     suma=suma+i
#     print(i)
# print(f"Suma najwiekszych liczb 3-cyfrowych podzielnych przez 37 to: {suma}")
# Zad.8
# suma=0
# n = int(input("Podaj ilosc elementow: "))
# for i in range(2,n*3,3):
#   if i%2==0:
#     suma=suma+i
#   elif i%2==1:
#     suma=suma-i
# print(f"Suma {n} elementow ciagu to: {suma}")
# Zad.9
# n=int(input("Podaj liczbe: "))
# x=0
# iloczyn=1
# for i in range(n):
#   if i%2==0:
#     x=2**i*(-1)
#   elif i%2==1:
#     x=2**i
#   iloczyn=iloczyn*x
# print(f"Iloczyn {n} pierwszych elementow ciagu to: {iloczyn}")
# Zad.10
# suma=0
# ilo=1
# n = int(input("Podaj liczbe: "))
# for i in range(1,n+1):
#   for j in range(1,i):
#     ilo=ilo*j
#     suma=suma+ilo
# print(suma)
# Zad.11 - procesor sie zapycha z niewiadomego powodu
# licznik = 0
# mianownik= 1
# n=int(input("Podaj n: "))
# l = -1
# iold=1
# lold=1
# a=0
# b=0
# c=0
# d=0
# e=0
# for i in range(1,n+1):
#   i=i*i
#   l=l+2
#   a=i
#   b=l
#   while a!=b:
#     c=a*b
#   while a!=b:
#     if a>b: 
#       a=a-b
#       c=c/a
#     elif b>a: 
#       b=b-a
#       c=c/b
#   a=c/i
#   b=c/l
#   d=c/iold
#   e=c/lold
#   i=i*a
#   l=l*b
#   iold=iold*d
#   lold=lold*e
#   i=i+iold
#   l=l+lold
#   licznik=licznik+l
#   mianownik=mianownik+i
#   iold=i
#   lold=l
# print(f"{licznik}/{mianownik}")
# Zad.12
# licznik =0
# mianownik=0
# l=-1
# n=int(input("Podaj ile ulamow dodajemy: "))
# for i in range(1,n+1):
#   l=l+2
#   i=i**2
#   licznik=licznik+l
#   mianownik=mianownik+i
# print(f"{licznik}/{mianownik}")
# Zad.13 i 14 bo są takie same
# n=int(input("Podaj n: "))
# suma=0
# licznik=0
# mianownik=1
# x=0
# l=0
# Zad.15
# n = int(input("Podaj ile ulamkow dodajemy: "))
# licznik = 1
# mianownik = 1
# l=2
# m=0
# for i in range(n):
#   m=m+2**i
#   l=l+1
#   licznik=licznik*l
#   mianownik=mianownik*m
# print(f"{licznik}/{mianownik}")
# Zad.16
ilo=0
n=int(input("Podaj ile ulamkow mnozymy: "))
a=0
b=1
f=0
m=0
for i in range(n):
  m=2**n
  