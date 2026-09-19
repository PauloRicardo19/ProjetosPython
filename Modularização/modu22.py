#Receba dois valores inteiros diferentes, mostre seus valores em ordem crescente (SEM PASSAGEM DE PARAMETRO)

No1: int = 0
No2: int = 0

def maior():
    if No1 > No2:
        print (No1, No2)
    else:
        print (No2, No1)

def main():
    global No1
    global No2
    No1 = int(input("Digite um número: "))
    No2 = int(input("Digite mais um número: "))
    maior()

if __name__ == '__main__':
    main()
    