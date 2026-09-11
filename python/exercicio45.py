#calcular e mostrar a serie 1 - 2/4 + 3/9 - 4/16 + 5/25 - .... + 15/225

Soma: float = 0.0 
for n in range(1,16):
    termo = n / (n ** 2)
    if n % 2 != 0:
        Soma = Soma + termo
    else:
        Soma = Soma - termo
print (Soma)