# Karty_pracy_py//KartaPracy7.py
import random
T = []
for i in range(40):
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