def f(n):
  wynik = 0
  for i in range(n):
    for j in range(n):
      if (i + j) % 2 == 0:
        wynik += 1
  return wynik

print(f(8))
