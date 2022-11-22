# 1 Algorytm sprawdzający czy liczba jest pierwsza
# WERSJA 1
# n = int(input("Podaj liczbe: "))
# for i in range(2,n):
#   if n%i==0:
#     print("Liczba nie jest pierwsza")
#     exit(0)
#   else:
#     print("Podana liczba jest pierwsza")
#     exit(0)

# WERSJA 2
# n = int(input("Podaj liczbe: "))
# Flaga=True
# for i in range(2,n):
#   if n%i==0:
#     Flaga=False
# if Flaga==False:
#   print("Podana liczba nie jest pierwsza")
#   exit(0)
# else:
#   print("Podana liczba jest pierwsza")
#   exit(0)

# WERSJA 3
# from math import sqrt
# n = int(input("Podaj n: "))
# for i in range(2,round(sqrt(n),0) + 1):
#   if n%i==0:
#     print("Liczba nie jest pierwsza")
#     exit(0)
#   else:
#     print("Liczba jest pierwsza")

# 2. Generator liczb pierwszych w przedziale [p,q]
# from math import sqrt
# p, q = map(int, input("Podaj 2 liczby: ").split())
# k = 1.0
# l=0
# for i in range(p,q+1):
#   flaga = True
#   k = sqrt(i)
#   l=round(k,0)
#   l=l+1
#   print(l)
#   for j in range(2, l):
#     if i % j == 0:
#       flaga = False
#   if flaga==True:
#     print(i, end=" ")

# 3.Generator liczb pierwszych - początkowe k liczb pierwszych 
# k = int(input("Podaj ile chcesz liczb pierwszych: "))
# x = 2
# while 1:
#   flaga = True
#   for i in range(2, int(x**0.5)+1):
#     if x % i == 0:
#       flaga = False
#   if flaga:
#     print(x, end=" ")
#     k = k-1
#     if k == 0:
#       break
#   x = x+1

# SPLIT
# m = "Niech zyje krol Julian".split()
# print(m)
# round((i**0.5),0)+1)