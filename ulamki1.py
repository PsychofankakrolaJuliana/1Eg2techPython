a = int(input("Podaj liczbe: "))
b = int(input("Podaj liczbe: "))
c = int(input("Podaj liczbe: "))
d = int(input("Podaj liczbe: "))
x = b
y = d
ilo = x*y
while y>0:
  x, y = y, x%y
nww = ilo // x
a=a*(nww/b)
print(f"{a}/{b}+{c}/{d}")