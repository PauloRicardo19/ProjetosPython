#Receber 3 valores OBRIGATORIAMENTE em ordem crescente, e um 4 fora de ordem, exibir os 4 em ordem crescente. (SEM PASSAGEM DE PARAMETRO)

N1: int = 0
N2: int = 0
N3: int = 0
N4: int = 0

def Ordem():
    global N1
    global N2
    global N3 
    global N4
    if not N1 <= N2 <= N3:
        print ("Os 3 primeiros PRECISAM estar em ordem.")
        exit()
    if N4 < N1:
            print (N4,N1,N2,N3)
    elif N4 < N2:
            print (N1,N4,N2,N3)
    elif N4 < N3:
            print (N1,N2,N4,N3)
    else:
            print (N1,N2,N3,N4)
    
def main():
    global N1
    global N2
    global N3 
    global N4
    N1 = int(input("Digite o 1o número: "))
    N2 = int(input("Digite o 2o número: "))
    N3 = int(input("Digite o 3o número: "))
    N4 = int(input("Digite o 4o número: "))
    Ordem()
if __name__ == '__main__':
    main()