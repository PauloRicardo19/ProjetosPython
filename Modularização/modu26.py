#recber dois numeros inteiros e verificar se o maior e multiplo do menor (SEM PASSAGEM DE PARAMETRO)

Num1: int = 0
Num2: int = 0
maior: int = 0
menor: int = 0

def calc():
    global Num1
    global Num2
    global maior
    global menor
    if Num1 > Num2:
        maior = Num1
        menor = Num2
    else:
        maior = Num2
        menor = Num1
    if maior % menor == 0:
        print ('O maior é multiplo do menor. ')
    else:
        print ('O maior não e multiplo do menor. ')

def main():
    global Num1
    global Num2
    Num1 = int(input("Digite o primeiro número: "))
    Num2 = int(input("Digite o segundo número: "))
    calc()

if __name__ == '__main__':
    main()