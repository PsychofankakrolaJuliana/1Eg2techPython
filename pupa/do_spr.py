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
