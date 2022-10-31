# *
# **
# ***
# n = int(input("Podaj n: "))
# for i in range(n):
#   for j in range(i+1):
#     print("*", end=" ")
#   print()

# ***
# **
# *
# n = int(input("Podaj n: "))
# for i in range(n):
#   for j in range(n-i):
#     print("*", end=" ")
#   print()

# Zad.1
# n = int(input("Podan n: "))
# for i in range(n) :
#   print("*-|"*i, end=" ")

# Zad.2
# n = int(input("Podaj n: "))
# for i in range(1,n):
#   for j in range(i,i+1):
#     if j%2==0 :
#       print("*"*j,"--", end=" ")
#     else:
#       print("*"*j,"||", end=" ")
  # Zad.3
# n = int(input("Podaj n: "))
# for i in range(n):
#   print
#   if i%2==1:
#     print("|"*i,"*", end=" ")
#   else:
#     print("-"*i, "*", end=" ")
# Zad.4
n = int(input("Podaj n: "))
for i in range(n):
  if i==0 or i==n-1:
    print("* "*n)
  else:
    print("*", " "*n, "*")
  # if n%2==0:
  #   if i==5 :
  #     print("*", " "*4, "*", " "*4, "*")
  # for j in range(i):
  #   print("* "*n, end=" ")
  #   print()