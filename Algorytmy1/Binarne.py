# Algorytmy1/Binarne.py
n=int(input("Podaj liczbę: "))
w=""
i=0
while n>0:
  n=n//2
  w=str(n%2)+w
  i+=1
print(w)
