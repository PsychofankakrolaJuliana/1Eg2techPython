# Stringi/stringi1.py
# String to taka jakby lista

# input napisu
s=input("Napisz napis: ")

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
L=list(s)
# L.sort()
print(L)

# przechodzenie z listy w napis
w="-".join(L) # <- to jest juz string, wywali napis z myślnikami
print(w)