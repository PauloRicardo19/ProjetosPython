#receba 100 numeros inteiros reais, mostra o maior e menor, somente positivos

N: float = 0.0
while N < 100:
    Num = float(input("Insira um numero: "))
    if N == 0:
        maior = Num
        menor = Num
    else:
        if Num > maior:
            maior = Num
        if Num < menor:
            menor = Num
    N = N + 1            
print ("O maior e:",maior)
print ("O menor e:",menor)        