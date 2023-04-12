# Zad.1
# a=input("Podaj wyraz: ")
# b=input("Podaj drugi wyraz: ")
# a=a.lower()
# b=b.lower()
# X=list(a)
# Y=list(b)
# n=0
# for i in range(len(Y)):
#   if Y[i]==X[0]:
#     for j in range(len(X)):
#       if Y[i+j]!=X[j]:
#         n=0
#       else:
#         n=1
#     break
# if n==1:
#   print("TAK")
# else:
#   print("NIE")
  
# Zad.2
# x=input("Napisz wyraz: ")
# x=x.lower()
# T=list(x)
# n=0
# for i in range(len(T)):
#   if T[i]=="a":
#     n+=1
#   elif T[i]=="b":
#     n+=1
#   elif T[i]=="z":
#     n+=1
# if n==4:
#   print("Da sie utworzyć słowo baza.")
# else:
#   print("Nie da się utworzyć słowa baza")

# Zad.3
# x=input("Podaj slowo: ")
# x=x.lower()
# T=list(x)
# L=T.copy()
# ilo=0
# for i in range(len(T)):
#   for j in range(len(L)):
#     if T[i]==L[j]:
#       ilo+=1
#   if ilo>1:
#     T.remove(T[i])
# x="".join(T)
# print(x)