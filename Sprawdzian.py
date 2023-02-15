l=int(input("Podaj licznik: "))
m=int(input("Podaj mianownik: "))
from math import ceil
n=ceil(l/m)
m2=l-1
r=l-n
l3=0
r2=0
l4=0
r3=0
if m2==1:
  print(f"{l}/{m}=1/{n}+{m2}/{r}")
else:
  r2=ceil(1/n)
  l3=1
  r3=n-r2
  l4=m2-l3
  if l4==1:
    print(f"{l}/{m}=1/{n}+{l3}/{r2}+{l4}/{r3}")