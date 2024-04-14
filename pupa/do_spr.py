# MONTE CARLO
# import random
# def monte_carlo_pi(i):
#     a = 0
#     b = i
#     for _ in range(i):
#         x = random.uniform(0, 1)
#         y = random.uniform(0, 1)
#         if x**2 + y**2 <= 1:
#             a += 1
#     pi = 4 * a / b
#     return pi

# pi = monte_carlo_pi(1000000)
# print("Przybliżona wartość liczby π (pi) za pomocą algorytmu Monte Carlo:", pi)

# LIDER

# wersja 1
# def lider1(ids):
#   cunts={}
#   for i in ids:
#     if i in cunts:
#       cunts[i]+=1
#     else:
#       cunts[i]=1;
#   lider = max(cunts, key=cunts.get)
#   return lider
# pussy=[8,2,1,1,4,4,5,6,6,4,7]
# lider_id=lider1(pussy)
# print(lider_id)

# wersja 2
# def lider2(ids):
#   lider=max(ids)
#   return lider
# cunts=[1,4,8,4,6,5,2]
# print(lider2(cunts))

# NEWTON-RAPHSON
# def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
#   x = x0
#   for _ in range(max_iter):
#       fx = f(x)
#       if abs(fx) < tol:
#           return x
#       f_prime_x = f_prime(x)
#       if f_prime_x == 0:
#           return None
#       x = x - fx / f_prime_x
#   return None

# def f(x):
#   return x**3 - 2*x - 5

# def f_prime(x):
#   return 3*x**2 - 2

# root = newton_raphson(f, f_prime, 3)
# if root is not None:
#   print("Przybliżony pierwiastek równania f(x)=0:", root)
# else:
#   print("Nie udało się znaleźć pierwiastka równania f(x)=0 w danej liczbie iteracji.")

# BISEKCJA
# def bisection_method(f, a, b, tol=1e-6, max_iter=100):
#   if f(a) * f(b) >= 0:
#       print("Nie można znaleźć pierwiastka w danym przedziale.")
#       return None
#   for _ in range(max_iter):
#       c = (a + b) / 2
#       if abs(b - a) < tol:
#           return c
#       if f(c) == 0:
#           return c
#       elif f(c) * f(a) < 0:
#           b = c
#       else:
#           a = c
#   print("Nie udało się znaleźć pierwiastka w danej liczbie iteracji.")
#   return None

# import math
# def f(x):
#   return x**3 - 2*x - 5
# root = bisection_method(f, 1, 3)
# if root is not None:
#   print("Przybliżony pierwiastek równania f(x)=0:", root)


# PROSTOKATY

# def f(x):
#   return 14 + 3 * x

# Nadmiar
# def main1(a, b, n):
#   dx = (b - a) / n
#   sum = 0
#   for i in range(n):
#     sum += f(a + i * dx + dx) * dx
#   return sum
# print(main1(2, 5, 4))

# Niedomiar
# def main2(a, b, n):
#   dx = (b - a) / n
#   sum = 0
#   for i in range(n):
#     sum = f(a + i * dx) * dx
#   return sum
# print(main2(2, 5, 4))

# Gówno (G->R)
# def main3(a, b, n):
#   dx = (b - a) / n
#   sum = 0
#   for i in range(n):
#     sum += f(a + i * dx + dx / 2) * dx
#   return sum
# print(main3(2, 5, 4))
