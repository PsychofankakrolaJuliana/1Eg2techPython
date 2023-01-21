# Karty_pracy_py//KartaPracy7.py
import random
for T in range(0, 40):
  print((random.randint(10, 99)), end=" ")
print("\n")

# Zad.1
maks=0
for i in range(T):
  if i>maks:
    maks=i
print(maks)