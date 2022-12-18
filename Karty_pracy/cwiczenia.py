# Karta Pracy 6a
# Zad.1
# x = int(input("Podaj liczbe wielocyfrową: "))
# suma=0
# while x>0:
#   suma=suma+x%10
#   x=x//10
# print(suma)
# Zad.2
# a = int(input("Podaj liczbe: "))
# flaga=True
# for i in range(2, a):
#   if a % i == 0:
#     flaga=False
# if flaga==True:
#   print("Podana liczba jest pierwsza")
# elif flaga==False:
#   print("Podana liczba nie jest pierwsza")
# Zad.3
# n = int(input("Podaj liczbe: "))
# suma=0
# for i in range(1,n):
#   if n%i==0:
#     suma+=i
# if suma==n:
#   print("Podana liczba jest doskonala")
# else:
#   print("Podana liczba nie jest doskonala")
# Zad.4
# a = int(input("Podaj liczbe: "))
# b = int(input("Podaj druga liczbe: "))
# x=a
# y=b
# while x!=y:
#   if x>y:
#     x=x-y
#   elif y>x:
#     y=y-x
# if x==1:
#   print("Podane liczby sa wzglednie pierwsze")
# else:
#   print("Podane liczby nie sa wzglednie pierwsze")
# Zad.5
# n = int(input("Podaj liczbe: "))
# x=n
# y=0
# for i in range(10,20):
#   i=y
#   while x!=y:
#     if x>y:
#       x=x-y
#     elif y>x:
#       y=y-x
#     if x==0:
#       print(i, end=" ")