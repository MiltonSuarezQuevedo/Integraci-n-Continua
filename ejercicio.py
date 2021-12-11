#Area de un circulo
print("Area de un circulo   ")
from math import pi

r = int(input("Digite radio    "))
def area_circulo(r):
  area = pi * r **2
  return area
print("el area del circulo es " , area_circulo(r))