def potega(a, n):
  w = 1
  while n > 0:
    if n % 2 == 1:
      w = w * a
    a = a * a
    n = n // 2
  return w

# print(potega(2,4))

def binnadec(b):
  d=0
  b2=list(reversed(b))
  for i in range(len(b2)):
    if b2[i]=='1':
      d+=2**i
  return d

# print(binnadec('101'))
  
def decnabin(d):
  b=""
  for i in range(d):
    if 2**i<=d:
      d-=2**i
      b+="1"
    else:
      b+="0"
    if d==0:
      break
  return b
  
# print(decnabin(31))
