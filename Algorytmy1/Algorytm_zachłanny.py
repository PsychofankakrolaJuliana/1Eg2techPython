# ALgorytmy1/Algorytm_zachłanny.py
# Algorytm zachłanny - algorytm człowieczy

# Wydawanie reszty: 
# kw=int(input("Podaj kwote: "))
# ilo=0
# x=0
# T=[500,200,100,50,20,10,5,2,1]
# while kw>0:
#   for i in T:
#     if T[i]<kw:
#       x=kw//T[i]
#       kw=kw-T[i]*x
#       print(f"{x}*{T[i]} ") 
#     x=0

# kw=int(input("Podaj kwote: "))
# ilo=0
# T=[500,200,100,50,20,10,5,2,1]]
# for i in T:
#   ilo=kw//i
#   kw=kw-ilo*i
#   print(f"{i}, {ilo}")

# kw=int(input("Podaj kwote: "))
# T=[500,200,100,50,20,10,5,2,1]
# ilo=0
# W=[]
# for i in T:
#   ilo=kw//i
#   if ilo>0:
#     kw=kw-ilo*i
#     for j in range(ilo):
#       W.append(i)
# # opcjonalnie zamiast appenda w forze: W=W+ilo*T[i]
# print(W)