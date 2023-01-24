# Karty_pracy_py//KartaPracy7.py
import random
T = []
for h in range(40):
  random_number = random.randint(10,99)
  T.append(random_number)
print(T, end=" ")
print("\n")

# Zad.1
# maks=0
# for i in range(0,len(T)):
#   if T[i]>maks:
#     maks=T[i]
# print(maks)

# print(max(T))

# Zad.2
# mn=100
# for i in range(len(T)):
#   if(T[i]<mn):
#     mn=T[i]
# print(mn)

# print(min(T)):

# Zad.3
# mn=100
# maks=0
# for i in range(len(T)):
#   if T[i]>maks:
#     maks=T[i]
# for i in range(len(T)):
#   if(T[i]<mn):
#     mn=T[i]
# x=maks-mn
# print(x)

# a=max(T)
# b=min(T)
# c=a-b
# print(c)

# Zad.6
# maks=0
# ilo=0
# for i in range(0,len(T)):
#   if T[i]>maks:
#     maks=T[i]
# for k in range(len(T)):
#   if T[k]==maks:
#     ilo+=1
# print(ilo)

# ilo=0
# x=max(T)
# for i in range(len(T)):
#   if T[i]==x:
#     ilo+=1
# print(ilo)

# Zad.7
# ilo=0
# mn=100
# for i in range(len(T)):
#   if(T[i]<mn):
#     mn=T[i]
# for k in range(len(T)):
#   if(T[k]==mn):
#     ilo+=1
# print(ilo)

# ilo=0
# x=min(T)
# for i in range(len(T)):
#   if T[i]==x:
#     ilo+=1
# print(ilo)

# Zad.8
# n = int(input("Podaj liczbe: "))
# ilo=0
# for i in range(len(T)):
#   if T[i]==n:
#     ilo+=1
# print(ilo)

# n=int(input("Podaj liczbe: "))
# ilo= T.count(n)
# print(ilo)

# Zad.9
# suma=0
# for i in range(len(T)):
#   suma+=T[i]
# suma=suma/40
# print(round(suma,1))

# Zad.10
# suma=0
# for i in range(0,len(T),2):
#   suma+=T[i]
# print(suma)

# Zad.11
# suma=0
# for i in range(1,len(T),2):
#   suma+=T[i]
# suma=suma//40
# print(suma)

# Zad.12
# x=0
# ilo=0
# for i in range(len(T)):
#   x=i
#   for k in range(len(T)):
#     if T[k]==x:
#       ilo+=1
#   if ilo==1:
#     print(T[i], end=" ")

# Zad.13
# f=1
# for i in range(10,100):
#   for j in range(len(T)):
#     if i==T[j]:
#       f=0
#   if f==1:
#     print(i)

# Zad.14         
# ilo=0
# for i in range(len(T)):
#   for j in range(len(T)):
#     if i==j:
#       ilo=ilo+1
# print(ilo)

