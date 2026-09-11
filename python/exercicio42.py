#calcule e mostre a sequencia 1 + 2/3 + 3/5 + ...... + 50/99

Soma: float = 1
numerador: int = 2
divisor: int = 3
while numerador <= 50:
    Soma = Soma + numerador / divisor
    numerador = numerador + 1
    divisor = divisor + 2
    print (Soma)