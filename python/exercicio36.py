#receba um numero calcule e mostre a sequencia 1 + 1/N! 

N = float(input("Digite um numero: "))
Soma: int = 1
Fat: int = 1
Contador: int = 1
while Contador <= N:
   Fat = Fat * Contador
   Soma = Soma + (1 / Fat)
   Contador = Contador + 1
print (Soma)
    