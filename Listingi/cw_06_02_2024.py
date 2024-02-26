# metoda prostokata - potrzebna jest funkcja oraz trzy warianty metody
def f(x):
  return -x**2 + 6 * x + 2


def prostokaty1(a, b, n):
  xd = (b - a) / n
  s = 0
  for i in range(n):
    s += f(a + i * xd / 2 + i * xd) * xd
  return s


def prostokaty2(a, b, n):
  xd = (b - a) / n
  s = 0
  for i in range(n):
    s += f(a + xd / 2 + i * xd) * xd
  return s


def prostokaty3(a, b, n):
  xd = (b - a) / n
  s = 0
  for i in range(n):
    s += f(a + xd + i * xd) * xd
  return s


def trapezy1(a, b, n):
  xd = (b - a) / n
  s = 0
  for i in range(n):
    s += (f(a + i * xd) + i * xd) + f(a + (i + 1)) * xd / 2
  return s


def trapezy2(a, b, n):
  xd = (b - a) / n
  s = 0
  for i in range(n):
    s += 2 * f(a + i * xd)
  return s * xd / 2
