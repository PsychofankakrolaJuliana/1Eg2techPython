# Cezar//Pre.py
# Szyfr Cezara
#  A B C D E F G H  I J K L M N O P Q R S T U V W X Y Z
# Funkcja ord - zwraca kod ascii dla danego znaku
# Funkcja chr - zwraca znak dla kodu ascii
# print(ord("M"))
# print(chr(69))
# Można połączyć
# print(chr(ord("C")+5))

# Napisz alfabet za pomocą pętli for
# for i in range(65,91):
#   print(chr(i), end=" ")

# Jak wydobyć literki z napisu
# napis = "Kret"
# print(len(napis))
# print(napis[0])

# pętla wyciągająca  znapisu literki
# napis = input("Napisz napis: ")
# for i in range(len(napis)):
#   print(napis[i], end=" ")

# napisz pętle wyciągającą kody ascii z napisu
# napis = input("Napisz napis: ")
# for i in range(len(napis)):
#   print(ord(napis[i]))

# zaszyfruj napis cezarem w kluczu = 3
# napis = input("Napisz napis: ")
# szyfr = ""
# for i in range(len(napis)):
#   szyfr = szyfr + chr(65 + (ord(napis[i]) - 65 + 3) % 26)
# print(szyfr)

# dodaj ułamki o różnych mianownikach
# a = int(input("Podaj liczbe: "))
# b = int(input("Podaj liczbe: "))
# c = int(input("Podaj liczbe: "))
# d = int(input("Podaj liczbe: "))
# e= 0
# f=0
# g=0
# h=0
# while a!=b:
#   if a>b: e=a-b
#   elif b>a: e=b-a
# while c!=d:
#   if c>d: f=c-d
#   elif d>c: f=d-c
# a=a/e
# b=b/e
# c=c/f
# d=d/f
# while a!=c: g=a*c
# while a!=b:
#   if a>b: 
#     a=a-c 
#     h=h/a
#   elif c>a: 
#     c=c-a
#     h=h/c
# while b!=d:
#   h=b*d
# while b!=d:
#   if b>d: 
#     b=b-d
#     h=h/a
#   elif d>b: 
#     d=d-b
#     h=h/d
# b=d
# a=c
# suma=0
# sum = 0
# suma = a+c
# sum = b+d
# print(suma,"/",sum)
