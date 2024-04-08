# Zad.1
# n = input("Podaj liczbe binarna: ")
# if(n[len(n)]=="1"):
#   print("Liczba jest parzysta")
# else:
#   print("Liczba jest nieparzysta")

# x=input()
# if(x[len(x)-1]=="0"):
#   print("Liczba jest parzysta")
# else:
#   print("Liczba jest nieparzysta")

# Zad.2

# SUMA
# a=input()
# b=input()
# if(a[len(a)]=="1" and b[len(b)]=="1"):
#   print("parzyste")
# if(a[len(a)]=="0" and b[len(b)]=="0"):
#   print("parzyste")
# else:
#   print("nieparzyste")

# c=input()
# d=input()
# if(c[len(c)]== d[len(d)]):
#   print("parzyste")
# else:
#   print("nieparzyste")

# e=input()
# f=input()
# if(e[-1]==f[-1]):
#   print("parzysta")
# else:
#   print("nieparzysta")

# ROZNICA
# a=input()
# b=input()
# if(a[len(a)]=="1" and b[len(b)]=="1"):
#   print("parzyste")
# if(a[len(a)]=="0" and b[len(b)]=="0"):
#   print("parzyste")
# else:
#   print("nieparzyste")

# c=input()
# d=input()
# if(c[len(c)]== d[len(d)]):
#   print("parzyste")
# else:
#   print("nieparzyste")

# e=input()
# f=input()
# if(e[-1]==f[-1]):
#   print("parzysta")
# else:
#   print("nieparzysta")

# ILOCZYN
# a = input()
# b = input()
# if (a[len(a)] == "1" or b[len(b)] == "1"):
#   print("nieparzyste")
# else:
#   print("parzyste")

# Zad.3
# a=input()
# b=input()
# wynik=""
# for i in range(len(a)):
#   if(a[i]=="1" and b[i]=="1"):
#     wynik+="01"
#   if(a[i]=="1" and b[i]=="0"):
#     wynik+="1"
#   if(a[i]=="0" and b[i]=="1"):
#     wynik+="1"
#   else:
#     wynik+="0"
# wynik.reverse()

# x = input()
# y = input()
# w = ""
# j = 0
# for i in range(len(x), -1, -1):
#   s = j + int(x[i]) + int(y[i])
#   j = s // 2
#   w = str(s % 2) + w
# if(j>0):
#   w = str(j) + w
# print(w)
