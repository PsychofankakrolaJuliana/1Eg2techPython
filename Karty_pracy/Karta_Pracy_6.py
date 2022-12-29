# Zad.1
# a = int(input("Podaj liczbe: "))
# b = int(input("Podaj drugom liczbe: "))
# c = int(input("Podaj trzeciom liczbe: "))
# if()
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