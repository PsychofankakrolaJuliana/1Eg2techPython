# Zad.1
# for i in range(1,31) :
#   print(i, end=" ")

# Zad.2
# for i in range(1,20,2) :
#   print(i*i, end=" ")

# Zad.3
# for i in range(1000,9999) :
#   if i%379==0 :
#     print(i, end=" ")

# Zad.4
# for i in range(100,1000) :
#   if i%5==0 and i%6==0 or i%11==0 :
#     print(i, end=" ")

# Zad.5
# n = int(input("Podaj ile liczb podasz: "))
# suma = 0
# for i in range(0,n) :
#   a = int(input("Podaj liczbe: "))
#   suma = suma+a
# print(suma)

# Zad.6
# k = int(input("Podaj ile liczb: "))
# for i in range(0,(k+1)*2,2) :
#   suma=i+i
# print(suma)

# Zad.7
# m = int(input("Podaj ile liczb: "))
# suma = 0
# for i in range(11,(11+m*2),2) :
#   suma=suma+i
# print(suma)

# Zad.8
w0 = float(input("Podaj kwote: "))
l = int(input("Podaj liczbe z dokładnoscia do pol roku: "))
m = l*12
w = w0
for i in range(1,m) :
  w = w + 0.005*w
print(round(w,2))