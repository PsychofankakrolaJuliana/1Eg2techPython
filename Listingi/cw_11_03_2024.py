# Lider
T=[1,2,1,3,1,1,4]
def lider():
  kandydat=T[0]
  ilosc=1
  for i in range(1,len(T)):
    if ilosc==0:
      kandydat=T[i]
      ilosc=1
    else:
      if T[i]==kandydat:
        ilosc+=1
      else:
        ilosc-=1
  ilosc_kandydatow=0
  if ilosc==0:
    print("Brak lidera")
  else:
    for i in range(len(T)):
      if T[i]==kandydat:
        ilosc_kandydatow+=1
  if ilosc_kandydatow>len(T)/2:
    print("Lider to: ",kandydat)
