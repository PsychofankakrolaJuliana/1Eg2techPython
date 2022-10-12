# ćwiczenie 1
# p = int(input("Daj liczbe "))
# q = int(input("Daj drugą liczbe "))
# if q * 0.3 == p:
#   print("TAK")
# else:
#   print("NIE")

# pętla 1
# for i in range(10,22): print(i, end="\n")
# pętla 2
# for i in range(15, 32, 2): print(i, end="\n")
# pętla 3
# for i in range(99, 10, -1): print(i, end=" ")
# pętla 4
# for i in range(10,100,1) : print(109-i, end=" ")
# pętla 5
# for i in range(100,1000,20) : print(i, end=" ")

# Zad.1
# n = int(input("Daj liczbe "))
# for i in range(n):
# print(i**3 + 3)

# Zad.2
# for i in range(105,1000,15) :
#   print(i, end=" ")

# Zad.3
# n = int(input("Daj liczbe: "))
# for i in range(1,n+1) :
#   if n % i == 0 :
#     print(i, end=" ")

# Zad.4
# suma = 0
# for i in range(10,100) :
#   suma = suma + i
# print(suma),

# Zad.5
# n = int(input("Podaj liczbe: "))
# suma = n*(n+1)//2
# for i in range(n-1):
#   x = int(input("Podaj liczbe: "))
#   suma = suma - x
# print("Nie podałeś: ",suma)

# Zad.6
# a = 0
# b = 1
# n = int(input("Podaj ile razy: "))
# print(a, end=" ")
# print(b, end=" ")
# for i in range(n+1):
#   a, b=b, a+b
#   print(b, end=" ")