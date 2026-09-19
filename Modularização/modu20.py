#calcular equaçao do segundo grau com raizes, verificando se ha raizes (SEM PASSAGEM DE PARAMETRO)

import math

A: float = 0.0
B: float = 0.0 
C: float = 0.0
Delta: float = 0.0


def calculo():
    global Delta
    Delta = (B * B) - (4 * A * C)
    if Delta < 0:
        print ("Não tem raizes reais.")
    else:
        X1 = (-B + math.sqrt(Delta)) / (2 * A)
        X2 = (-B - math.sqrt(Delta)) / (2 * A)
        print ("A primeira raiz é:",X1)
        print ("A segunda raiz é:",X2)

def main():
    global A 
    global B
    global C
    A = float(input("Insira o Valor de A: "))
    B = float(input("Insira o Valor de B: "))
    C = float(input("Insira o Valor de C: "))
    calculo()

if __name__ == '__main__':
    main()