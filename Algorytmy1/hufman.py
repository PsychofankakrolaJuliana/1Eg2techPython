# Algorytmy1//hufman.py
W="AABCCCDDDDEFGGGHHIJJ"
E="2AB3C4DEF3G2HI2J"
H=""
ilo=1
for i in range(len(W)-1):
  if W[i]==W[i+1]:
    ilo=ilo+1
  else:
    if ilo>1:
      H=H+str(ilo)
    H=H+W[i]
    ilo=1
print(W)
print(H)