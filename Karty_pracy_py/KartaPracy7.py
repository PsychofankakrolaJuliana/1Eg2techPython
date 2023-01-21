# Karty_pracy_py//KartaPracy7.py
import random
T=[0]
for j in range(0, 40):
  T[j]=random.randint(10, 99)
print("\n")

# Zad.1
maks=0
for i in range(0,len(T)):
  if i>maks:
    maks=i
print(maks)