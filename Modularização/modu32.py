#o main recebe um numero inteiro, retorna o fatorial 

def Calc (N):
    Contador: int = 1
    while N >= 1:
        Contador = Contador * N 
        N = N - 1
    return Contador




def main ():
    Número: int = 0
    Número = int(input("Digite um número: "))
    Fatorial = Calc (Número)
    print ('O Fatorial de',Número,'é:',Fatorial)

if __name__ == '__main__':
    main ()