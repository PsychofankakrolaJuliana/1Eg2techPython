# ALgorytmy1/Algorytm_zachłanny.py
# Algorytm zachłanny - algorytm człowieczy

# Wydawanie reszty: 
kw=int(input("Podaj kwote: "))
ilo=0
x=0
T=[500,200,300,100,50,20,10,5,2,1]
while kw>0:
  for i in range(0,len(T),-1):
    if T[i]<kw:
      x=kw//T[i]
      print(f"{x}*{T[i]} ")

# kw=int(input("Podaj kwote: "))
# ilo=0
# T=[50,20,10,5,2,1]
# for i in T:
#   ilo=kw//i
#   kw=kw-ilo*i
#   print(f"{i}, {ilo}")