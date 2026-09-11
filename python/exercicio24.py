#receba um valor inteiro verifique e mostre se 'e divisivel por 2 e 3

Num = int(input("Qual o numero? "))
if (Num % 2 == 0) and (Num % 3 == 0):
    print ("E divisivel por 2 e 3")
else:
    print ("Nao e divisivel por 2 e 3")