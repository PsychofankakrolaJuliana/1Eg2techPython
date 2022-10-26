# Zad.1
# n = int(input("Podaj n: "))
# for i in range(n) :
#   print("*-|", end=" ")
# Zad.2
# n = int(input("Podaj n: "))
# for i in range(1,n+1) :
#   print("*"*i, end=" ")
#   if i%2==1 :
#     print("||", end=" ")
#   else :
#     print("--", end=" ")
# Zad.3
# n = int(input("Podaj n: "))
# for i in range(1,n+1):
#   print("*", end=" ")
#   if i%2==1 :
#       print("--"*i, end=" ")
#   else :
#       print("|"*i, end=" ")
# Zad.4
# n = int(input("Podaj n: "))
# print("*")
# for i in range(0,n) :
#   print(" "*n, "*", end=" ")
#   print(" "*i, end=" ")
#   print("*")
# for j in range(n,0,-1):
#   print(" "*n, "*", end=" ")
#   print(" "*j, end=" ")
#   print("*")
# print(" "*j, "*")

# for i in range(1,11):
#   for j in range(1,11) :
#     print(i*j, end="\t")

# 2 petle
# *
# **
# ***
n=int(input("Podaj n: "))
h=int(input("Podaj h: "))
for i in range(n):
  for j in range(i+1):
    print("*", end=" ")
  print()
print("* "*h)

# ***
# **
# *
for i in range(n):
   for j in range(n-i):
     print("*", end=" ")
   print()