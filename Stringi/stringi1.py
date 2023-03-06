# Stringi/stringi1.py
# String to taka jakby lista

# input napisu
# s=input("Napisz napis: ")

# print stringa
# for x in s:
#   print(x)

# for i in range(len(s)):
#   print(s[i])

# napis to nielista sensu stricte
# L=[7,4,5,2]
# L.sort()
# s.sort() -> tobedzie blad
# print(s,L)

# przechodzenie z napisu w liste
# L=list(s)
# L.sort()
# print(L)

# przechodzenie z listy w napis
# w="-".join(L) # <- to jest juz string, wywali napis z myślnikami
# print(w)

# Zad.1
#  sprawdx czy pisane slowo jest palindromem
# s=input("Napisz napis: ")
# L=list(s)
# X=L.copy()
# X.reverse()
# if X==L:
#   print("Tak")
#   a="".join(L)
#   print(a)
# else:
#   print("Nie")
#   print(L)
#   print(X)

# s=input("Napisz cos: ")
# for i in range(len(s)//2):
#   if s[i]!=s[len(s)-1-i]:
#     exit("NIE")
# exit("TA")

# L=[i for i in range(1,10)]
# print(L)
# print(L[:4])
# print(L[6:9:2])
# L=[start:stop:step]

# Anagramy przez sortowanie
# a=input("Napisz: ")
# b=input("Napisz: ")
# X=list(a)
# Y=list(b)
# X.sort()
# Y.sort()
# a="".join(X)
# b="".join(Y)
# print(a," ",b)
# if a==b:
#   print("TA")
# else:
#   print("NIE")

# Anagram przez tablice
a=input("Napisz: ")
b=input("Napisz: ")
X, Y=[0]*150,[0]*150
for i in range(len(a)):
  X[ord(a[i])]+=1
for i in range(len(b)):
  Y[ord(a[i])]+=1
if X==Y:
  print("TA")
else:
  print("NIE")

# Obliczanie wartości wyrażenia w ONP
3521+*+=
# jeśli mamy liczbe to na stos
# jeśli mamy działanie 