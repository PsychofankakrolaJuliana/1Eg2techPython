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
n = int(input("Podaj n: "))
for i in range(1,n+1):
  for j in range(1,n+1) :
    # if j==1 and (n%2==0 and i==n/2) or (n%2>0 and i==n/2+0.5) :
    if i==n or j==i:
      print("*",  end=" ")
    # elif i==1 and (n%2==0 and j==n/2) or (n%2>0 and j==n/2+0.5):
    elif j==i:
      print("*", end=" ")
    else:
      print("-", end=" ")
  print()
# Zad.5
# n = int(input("Podaj n: "))
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if (n%2==0 and j==n/2) or (n%2>0 and j==n/2+0.5):
#       print("*", end=" ")
#     elif (n%2==0 and i==n/2) or (n%2>0 and i==n/2+0.5):
#         print("-", end=" ")
#     else:
#       print(" ", end=" ")
#   print()
# Zad.6
# n=int(input("Podaj n: "))
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if i==n-j+1:
#       print("?", end=" ")
#     elif i==j:
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()
    
# Zad.7
# n = int(input("Podaj n: "))
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if i==1 or j==1 or i==n or j==n or (n%2>0 and i==n/2+0.5 and j==n/2+0.5) or (n%2==0 and i==n/2 and j==n/2):
#       print("*", end=" ")
#     else:
#       print(" ", end=" ")
#   print()

# for i in range(1,11):
#   for j in range(1,11) :
#     print(i*j, end="\t")

# 2 petle
# *
# **
# ***
# n=int(input("Podaj n: "))
# # h=int(input("Podaj h: "))
# for i in range(n):
#   for j in range(i+1):
#     print("*", end=" ")
#   print()
# # print("* "*h)

# ***
# **
# *
# n = int(input("Podaj n: "))
# for i in range(n):
#    for j in range(n-i) :
#      print("*", end=" ")
#    print()

#   *
#  **
# ***
# n = int(input("Podaj n: "))
# for i in range(n):
#   for j in range(n-i-1):
#     print(" ", end=" ")
#   for k in range(n-i-1,n):
#     print("*", end=" ")
#   print()

# ***
#  **
#   *
# n = int(input("Podaj n: "))
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if i==n-j+1:
#       print("*", end=" ")
#     elif j==n-i:
#       print("?", end=" ")
#     else:
#       print(" ", end=" ")
#   print()