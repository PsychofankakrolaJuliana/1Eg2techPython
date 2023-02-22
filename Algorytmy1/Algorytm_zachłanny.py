# ALgorytmy1/Algorytm_zachłanny.py
# Algorytm zachłanny - algorytm człowieczy

# Wydawanie reszty: 
kw=int(input("Podaj kwote: "))
ilo=0
x=0
T=[1,2,5,10,20,50,100,200,500]
while kw>0:
  for i in T:
    if T[i]>kw:
      x=kw//T[i]
      print(f"{x}*{T[i]} ")