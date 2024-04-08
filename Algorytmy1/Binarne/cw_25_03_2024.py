# Algorytmy1/Binarne.py


# ITERACJA
def dec2bin(n):
  w = ""
  while n > 0:
    n = n // 2
    w = str(n % 2) + w
    return w


# REKURENCJA
def dec2binreku(n):
  if n == 2:
    return ""
  else:
    return dec2binreku(n // 2) + str(n % 2)


def dec2binreku2(n):
  if n == 0:
    return ""
  dec2binreku2(n // 2)
  print(n % 2, end="")


print(dec2bin(27))
print(dec2binreku(27))
print(dec2binreku2(27))


# ITERACJA
def bin2dec(n):
  n.reverse()
  w = 0
  for i in range(len(n)):
    if (n[i] == "1"):
      w = w + 2**i
  return w


def bin2dec2(n):  #Schemat Hornera - nie obowiazkowe
  w = 0
  for i in range(len(n)):
    w = w * 2 + int(n[i])
  return w


def bin2dec3(n):
  w = 0
  for i in range(len(n)):
    w = w * 2 + int(n[-i - 1])
  return w
