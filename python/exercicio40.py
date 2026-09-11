#dois numeros inteiros e mostrar os numeros primos entre eles

A = int(input("Insira o 1o numero: "))
B = int(input("Insira o 2o numero: "))
if A > B:
    maior = A
    menor = B
else:
    maior = B
    menor = A
num = menor
while num <= maior:
    divi = 0
    i = 1
    while i <= num:
        if num % i == 0:
            divi = divi + 1
        i = i + 1
    if divi == 2:
        print (num)
    num = num + 1