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

# Zad.5
n = int(input("Podaj n: "))
for i in range(1,n+1):
  for j in range(1,n):
    if (n%2==0 and j==n/2+1) or (n%2>0 and j==n/2+0.5)  :
      print("*", end=" ")
    elif (n%2==0 and i==n/2+1) or (n%2>0 and i==n/2+0.5) :
      print("-", end=" ")
    else:
      print(" ", end=" ")
  print()

# Zad.7
# n = int(input("Podaj n: "))
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if i==1 or j==1 or i==n or j==n or (n%2>0 and i==n/2+0.5 and j==n/2+0.5) or (n%2==0 and i==n/2 and j==n/2):
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()