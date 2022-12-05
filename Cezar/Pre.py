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