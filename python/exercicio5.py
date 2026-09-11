#calcular raizes reias usando equaçao do segundo grau

import math

a = (float(input("Qual o valor de A?: ")))
b = (float(input("Qual o valor de B?: ")))
c = (float(input("Qual o valor de C?: ")))
delta = (b * b) - (4 * a * c)

x1 = float(-b + math.sqrt(delta)) / (2 * a)
x2 = float(-b - math.sqrt(delta)) / (2 * a)

print("x1",x1)
print("x2",x2)