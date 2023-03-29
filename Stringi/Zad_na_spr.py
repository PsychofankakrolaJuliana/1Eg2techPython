# Stringi/Zad_na_spr.py

# Zad.1
# n=input("Napisz napis: ")
# m=list(n)
# y=m.pop()
# x=m[0]
# print(x," ",y)

# Zad.2
# napis=input("Napisz napis: ")
# n=list(napis)
# for i in range(1,len(n)-1):
#   print(n[i])

# Zad.3
# napis=input("Napisz napis: ")
# n=list(napis)
# x=n.reverse()
# for i in range(0,4):
#   print(x[i])

# Zad.4
# napis=input("Napisz napis: ")
# suma=0
# T=list(napis)
# for i in range(len(T)):
#   suma=suma+ord(T[i])
# print(suma)

# Zad.5
# napis=input("Napisz napis: ")
# T=list(napis)
# ilo=0
# for i in range(len(T)):
#   if T[i]=="a":
#     ilo+=1
# print(ilo)

# Zad.6
# ilo=0
# ilo2=0
# napis=input("Napisz napis: ")
# T=list(napis)
# x=""
# for i in range(len(T)):
#   for j in range(len(T)):
#     if T[i]==T[j]:
#       ilo+=1
#     if ilo>ilo2:
#       ilo2=ilo
#       x=T[i]
# print(x)

# Zad.7
# n=input("Napisz napis: ")
# T=list(n)
# T.sort()
# L = list()
# ilo=0
# ilo2=0
# for k in range(len(T)):
#   for i in range(len(T)):
#     for j in range(len(T)):
#       if T[i]==T[j]:
#         ilo+=1
#   if(ilo>=ilo2):
#     L.append(T[i])
# print(L)

# def f(L, n):
#   for x in L:
#     if 0<L.count(x)<n:
#       return True
#   return False

# g=input("Napisz: ")
# K= [0]*100
# for x in g:
#   K[ord(x)]+=1
# domi=max(K)
# if sum(K)==max(K):
#   print("Dominanta: ", chr(K.index(max(K))))
# elif not f(K):
#   print("Brak dominanty :(")
# else:
#   D=[]
#   for i in K:
#     if K[i]==max(K):
#       D.append(chr(i))
#   print("Dominanty: ", ", ", join(D))

# Zad.8
# n=input("Napisz napis: ")
# T=list(n)
# ilo=0
# for i in range(len(n)-1):
#   j=i+1
#   if (T[i]=="l" and T[j]=="a") or (T[i]=="L" and T[j]=="A") or (T[i]=="L" and T[j]=="a") or (T[i]=="l" and T[j]=="A"):
#       ilo+=1
# if ilo >=3:
#   print("Tak, ", ilo)
# else:
#   print("Nie")

# x=0
# i=0
# while i>-1:
#   print(x)
#   x=x+1

# Zad.
# n = input("Napisz napis: ")
# T = list(n)
# x = 0
# L = []
# suma = 0
# for i in range(len(T)):
#   L.append(ord(T[i]))
#   x += 1
# for j in range(len(L)):
#   suma = suma + L[i]
# suma = suma / x
# suma = suma - (suma % 10)
# suma = chr(suma)
# print(suma)