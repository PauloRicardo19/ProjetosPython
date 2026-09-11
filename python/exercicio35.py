#receber dois valores inteiros, mstrar o maior e a soma entre os valores impares

N1 = int(input("Qual o 1o numero? "))
N2 = int(input("Qual o 2o numero? "))
Soma: int = 0
if N1 > N2:
    Maior = N1
    Menor = N2
else:
    Maior = N2
    Menor = N1
Impar = Menor
while Impar <= Maior:
    if Impar % 2 == 1:
        Soma = Soma + Impar
    Impar = Impar + 1
print ("Maior:",Maior)
print ("Soma dos Impares:",Soma)