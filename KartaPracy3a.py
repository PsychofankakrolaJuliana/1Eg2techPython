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
# Zad.5
n = int(input("Podaj n: "))
for i in range(1,n) :
  print("*", end=" ")
  print(" "*i, end=" ")
  print("*")

# for i in range(1,11):
#   for j in range(1,11) :
#     print(i*j, end="\t")