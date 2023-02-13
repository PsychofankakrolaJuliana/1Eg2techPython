# Algorytmy1//Algorytm_RSA.py

# # Funkcja na NWD
# from math import gcd
# print(gcd(12,16))

# # 1.Wybór 2 dużych liczb pierwszych
# p=11
# q=13
# print(p," ",q)
# # 2.FStworzenie funkcji f i znalezeienie n=p*q
# F=(p-1)*(q-1)
# n=p*q
# print(F," ",n)
# # 3.Znalezienie klucza publicz nego e: NWD(F,e)=1
# from math import gcd
# for i in range(2,F):
#   if gcd(i,F)==1:
#     e=i
#     break
# print(f"Klucz publiczny: {e} i {n}")
# # 4.Wygenerowanie klucza prywatnego d: (d*e)%n=1 (odwrotność modulo)
# d=0
# for j in range(2,n):
#   if (j*e)%F==1:
#     d=j
#     break
# print(d," ",n)

# # PRZYKŁAD DZIAŁANIA KODOWANIA ZNAKU X:
# # c=(x**e)%n (szyfr)
# # t=(c**d)%n (tekst jawny)
# msg=input("Napisz cos: ")
# szyfr=""
# for i in msg:
#   szyfr+=chr((ord(i)**e)%n)
# print(szyfr)

# jawny=""
# for j in szyfr:
#   jawny+=chr((ord(j)**d)%n)
# print(jawny)

# p=11
# q=13
# F=(p-1)*(q-1)
# n=p*q
# from math import gcd
# for i in range(2,F):
#   if gcd(i,F)==1:
#     e=i
#     break
# d=0
# for j in range(2,n):
#   d=j
#   break
# msg=input("Napisz coś: ")
# szyfr=""
# for i in msg:
#   szyfr+=chr((ord(i)**e)%n)
# print(szyfr)
# jawny=""
# for j in szyfr:
#   jawny+=chr((ord(j)**d)%n)
# print(jawny)