#receba um numero e mostre a serie 1 + 1/2! + 1/3! + 1/N!

def Calc (N):
    Contador: int = 1
    while N >= 1:
        Contador = Contador * N 
        N = N - 1
    return Contador

def DIV (Nu, F):
    return (Nu / F)



    


def main():
    Num: int = 0
    Num = int(input("Digite um número: "))
    cont: int = 1
    soma: float = 1.0
    while cont <= Num:
        Fat = Calc(cont)
        soma = soma + DIV(1,Fat)
        cont = cont + 1

    print ('A resposta é:',soma)


if __name__ == '__main__':
    main()