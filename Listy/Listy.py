# # Printowanie listy
# x=list(range(5))
# for item in x:
#   print(item, end=" ")


# # Len
# for i in range(len(x)):
#   print(x[i], end=" ")

# # print(len(x))

# # Printowanei całej listy
# L = [1,2,3,4,5]
# for elem in L:
#   print(elem, end=" ")
# for i in range(len(L)):
#   print(L[i], end=" ")

# # Funkcje w lisatch
# K=[4,7,5,7,3,3,2,8,7]
# print(K)

# K.append(3)
# print(K)

# print(K.count(7))

# print(K.index(7))

# K.insert(2,4)
# print(K)

# K.pop()
# print(K)

# K.pop(2)
# print(K)

# K.reverse()
# print(K)

# K.sort(reverse=True)
# print(K)

# # Usunąć wszystkie 7 z listy
# for i in range(K.count(7)):
#   K.remove(7)
# print(K)

# for i in range(K.count(7)):
#   K.pop(K.index(7))
# print(K)

# Znajdz maxa w tablicy
# print(max(K))

# maks=K[0]
# for i in K:
#   if(i>maks):
#     maks=i
# print(maks)

# maks=K[0]
# for i in range(len(K)):
#   if(K[i]>maks):
#     maks=K[i]
# print(maks)

# # Zakresy
# L=[3,7,2,1,5,4,2,4,8]
# range(2,10,3) 