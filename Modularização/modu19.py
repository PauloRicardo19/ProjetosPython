#Receba dois valores reais, calcule e mostre o maior deles (SEM PASSAGEM DE PARAMETRO)

num1: float = 0.0
num2: float = 0.0

def maior():
    if num1 > num2:
        print (num1)
    else:
        print (num2)

def main():
    global num1
    num1 = float(input("Insira um valor: "))
    global num2
    num2 = float(input("Insura outro valor: "))
    maior()

if __name__ == '__main__':
    main()
