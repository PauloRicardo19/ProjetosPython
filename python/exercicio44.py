#receba a base e o expoente mostre a potencia.

Base = int(input("Insira o valor da base: "))
Expoente = int(input("Insira o valor do expoente: "))
resultado: int = 1
contador: int = 1
while contador <= Expoente:
    resultado = resultado * Base
    contador = contador + 1
    print (resultado)

