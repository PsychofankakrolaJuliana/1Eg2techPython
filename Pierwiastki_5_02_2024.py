i = int(input("Podaj pole: "))
p = int(input("Podaj ilość kroków: "))

# Sposób.1:
def NR(P, n):
  a = P / n
  b = 1
  for i in range(n):
    a = (a + b) / 2
    b = P / a
  return a
print(NR(i, p))

# Sposób.2:
def NR2(P2, n2):
  a2 = P2
  b2 = 1
  for i2 in range(n2):
    a2 = (a2 + b2) / 2
    b2 = P2 / a2
  return a2
print(NR2(i, p))

# Sposób.3:
def NR3(x, eps):
  a = x
  b = 1
  while abs(a - b) > eps:
    a = (a + b) / 2
    b = x / a
  return a
print(NR3(i, p))
