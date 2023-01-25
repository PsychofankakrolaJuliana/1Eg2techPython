# Algorytmy1//Algorytm_RSA.py

# Funkcja na NWD
# from math import gcd
# print(gcd(12,16))

# 1.Wybór 2 dużych liczb pierwszych
p=11
q=13
print(p," ",q)
# 2.FStworzenie funkcji f i znalezeienie n=p*q
F=(p-1)*(q-1)
n=p*q
print(F," ",n)
# 3.Znalezienie klucza publicznego e: NWD(F,e)=1
from math import gcd
for i in range(2,F):
  if gcd(i,F)==1:
    e=i
    break
print(i)