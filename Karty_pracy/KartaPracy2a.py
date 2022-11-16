# Zad.1
a = int(input("Daj liczbe: "))
b = int(input("Daj drugom liczbe: "))
if (a+b)%2==0 :
  print("Suma jest parzysta")
else :
  print("Suma nie jest parzysta")

# Zad.2
import math
a = int(input("Daj liczbe: "))
b = int(input("Daj drugom liczbe: "))
art = (a+b)/2
g = math. sqrt(a*b)
if art > g :
  print("TAK")
else :
  print("NIE")

# Zad.3
k = int(input("Daj liczbe: "))
l = int(input("Daj drugom liczbe: "))
m = int(input("Daj trzeciom liczbe: "))
if k == m :
  print("Tak, ", k,m)
if m == l :
  print("Tak, ", m,l)
if k == l :
  print("Tak, ", k,l)
if k != m and k != l and m != l :
  print("Nie")
else :
  print("Wszytskie są równe")
  
# Zad.4
a = int(input("Daj liczbe: "))
b = int(input("Daj drugom liczbe: "))
c = int(input("Daj trzeciom liczbe: "))
d = int(input("Daj czwartom liczbe: "))
licznik = 0
if a ==  b or b==c or a==c or a==d or b==d or c==d :
  print("Nie wszystkie liczby są rurzne")
else :
  min = None
  list = [a,b,c,d]
  for i in list :
    licznik=licznik+1
    if licznik == 1 :
      min=i
    elif licznik > 1 :
      if min > i :
        min = i
  print("Najmniejsza liczba to ", min)

# Zad.5
a = int(input("Daj liczbe: "))
b = int(input("Daj drugom liczbe: "))
c = int(input("Daj trzeciom liczbe: "))
if c<a+b and a<b+c and b<a+c :
  print("Podane liczby spelniaja nierownosc trojkata")
else :
  print("Liczby nie spelniaja nierownosci trojkata")

# Zad.6
a = int(input("Daj przyprostokatna: "))
b = int(input("Daj drugom przyprostokatna: "))
c = int(input("Daj przeciwprostokatna: "))
if c<a+b :
  if c**2==a**2+b**2 :
    print("Trojkat bedzie prostokatny")
  elif c**2<a**2+b**2 :
    print("Trojkat bedzie ostrokatny")
  else :
    print("Trojkat bedzie rozwartokatny")
else :
  print("Z podanych bokow nie da sie utworzyc trojkata")