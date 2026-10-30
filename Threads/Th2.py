import multiprocessing 
import time
import random

def processa(id, numeros):
    soma: int = 0 
    i: int = 0
    for i in range (0,5,1):
        soma = soma + numeros[i]
        time.sleep(0.2)
    print ('ID #',id,'Soma',soma)


def main():
    ID: int = 0
    cont: int = 0
    Vetor1: int = [0]*5
    Vetor2: int = [0]*5
    Vetor3: int = [0]*5
    parametros: int = [(0,0)]*3
    for cont in range (0,5,1):
        Vetor1[cont] = random.randint(1,100)
    parametros[0] = (1, Vetor1)
    for cont in range (0,5,1):
        Vetor2[cont] = random.randint(1,100)
    parametros[1] = (2, Vetor2)
    for cont in range (0,5,1):   
        Vetor3[cont] = random.randint(1,100)
    parametros[2] = (3, Vetor3)
 
    with multiprocessing.Pool(processes=3) as threads:
       threads.starmap(processa, parametros)



if __name__ == '__main__':
    main()
    