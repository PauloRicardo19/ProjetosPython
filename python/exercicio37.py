#Calcula Fibonacci ate o N'nesimo termo

Num = int(input("Digite o termo: "))
A: int = 0
B: int = 1
contador: int = 0
while contador < Num:
    print (A)
    prox = A + B 
    A = B
    B = prox
    contador = contador + 1
