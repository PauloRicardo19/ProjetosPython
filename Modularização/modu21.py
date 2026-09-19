#receber 4 notas bimestrais, calcular media aritmetica e mostrar diferentes resultados (SEM PASSAGEM DE PARAMETRO)

N1: float = 0.0
N2: float = 0.0 
N3: float = 0.0 
N4: float = 0.0 
MediaAritmetica: float = 0.0

def mediaAri():
    global MediaAritmetica
    MediaAritmetica = (N1 + N2 + N3 + N4) / 4
    if MediaAritmetica >= 6.0:
        print ('APROVADO')
    elif MediaAritmetica >= 3.0 and MediaAritmetica < 6.0:
        print ('EXAME')
    else:
        print ('RETIDO')

def main():
    global N1
    global N2
    global N3
    global N4
    N1 = float(input("Digite a Nota 1: "))
    N2 = float(input("Digite a Nota 2: "))
    N3 = float(input("Digite a Nota 3: "))
    N4 = float(input("Digite a Nota 4: "))
    mediaAri()

if __name__ == '__main__':
    main()

    