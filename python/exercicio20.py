#calcular equaçao do segundo grau com raizes 

import math

A = float(input("Insira o valor de A: "))
B = float(input("Insira o valor de B: "))
C = float(input("Insira o valor de C: "))
Delta = (B * B) - (4 * A * C)
if Delta < 0: 
    print ("Nao ha raizes reais")
else:
    X1 = (-B + math.sqrt(Delta)) / (2 * A)
    X2 = (-B - math.sqrt(Delta)) / (2 * A)
    print ("A primeira raiz e:",X1)
    print ("A segunda raiz e:",X2)