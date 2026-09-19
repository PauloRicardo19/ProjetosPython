#Receber um valor inteiro e verificar se e divisivel por 2 e 3. (SEM PASSAGEM DE PARAMETRO)

N1: int = 0

def div():
    global N1
    if N1 % 2 ==0 and N1 % 3 == 0:
        print (N1,'É divisivel por 2 e 3.')
    else:
        print (N1,'Não é divisivel por 2 e 3')

def main():
    global N1
    N1 = int(input("Digite um valor: "))
    div()

if __name__ == '__main__':
    main()
    