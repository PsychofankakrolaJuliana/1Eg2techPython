# Zad.1
x  = int(input("Podaj liczbę: "))
suma=0
while x>0:
  suma=suma+x%10
  x=x//10
print(suma)