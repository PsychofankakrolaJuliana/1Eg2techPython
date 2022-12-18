# Karta Pracy 6a
# Zad.1
# x = int(input("Podaj liczbe wielocyfrową: "))
# suma=0
# while x>0:
#   suma=suma+x%10
#   x=x//10
# print(suma)
# Zad.2
a = int(input("Podaj liczbe: "))
while a > 0:
  for i in range(2, a):
    if a % i == 0:
      print("Podana liczba nie jest pierwsza")
      break
    else:
      print("Podana liczba jest pierwsza")