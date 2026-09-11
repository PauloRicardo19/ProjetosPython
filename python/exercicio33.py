#receba um numero e mostre a serie 1 + 1/2 + 1/3 + 1/N

Soma: float = 0
Contador: float = 1
Num = float(input("Insira um numero: "))
while Contador <= Num:
    Soma = Soma + (1 / Contador)
    Contador = Contador + 1
print (Soma)