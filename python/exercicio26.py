#Receber dois numeros inteiros verificar se o mair e multiplo do menor

Num1 = int(input("Qual o 1o numero? "))
Num2 = int(input("Qual o 2o numero? "))
if Num1 > Num2:
    Maior = Num1
    Menor = Num2
else:
    Maior = Num2
    Menor = Num1
if Maior % Menor == 0:
    print ("O maior e multiplo do menor.")
else:
    print ("O maior nao e multiplo do menor.")