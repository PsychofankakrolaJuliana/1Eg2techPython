D = {}  #pusty slownik

n=int(input("Daj liczbe: "))
m=int(input("Daj druga liczbe: "))

for i in range(n):
  D[i + 1] = []
  # D.update({ i+1 : [] })

for _ in range(m):  #petla bez zmiennej
  p=int(input("Daj p: "))
  q=int(input("Daj q: "))      
  D[p].append(q)
  D[q].append(p)
# print(D)

# for i in range(1, n + 1):
#   if len(D[i]) == 0:
#     print("Wiewiór sam")
#   else:
#     D[i].sort()
#     for j in range(len(D[i])):
#       print(D[i][j], end=" ")
#     print()

# policz sumę stopni wierzechołków grafu
# suma = 0
# for k,v in D:
#   suma = suma + len(v)
# print(suma)

# znajdź wierzchołek o najwyższym stopniu
# maks=0
# for k,v in D:
#   if len(v)>maks:
#     maks=len(v)
# print(maks)

# znajdź wierzchołki samodzielne

# Sprawdź czy uda się dojść z wierzchołka x do y
# def DFS(n,D,vis=[]):
#   if vis==None:
#     vis=list()
#     if n not in vis:
#         vis.append(n)
#     else:
#       return 
#     for nei in D[n]:
#       DFS(nei, D, vis)
#     return vis
# visited=[]
# W=DFS(1,D,visited)
# print(W)
