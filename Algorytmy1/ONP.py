n=input("Wpisz cos: ")
S=[]
T=[]
for i in range(len(n)):
  if(i=="+" or i=="-" or i=="*" or i=="/"):
    S+=i
  else:
    T+=i
T.reverse
