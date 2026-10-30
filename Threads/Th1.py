import multiprocessing 
import time

def processa(id):
    time.sleep(0.5)
    print ("Thread #",id)


def main():
    identificador: int = 0
    contador: int = 0
    parametros: int = [0]*5
    for contador in range (0,5,1):
        identificador = contador + 1
        parametros[contador] = identificador 

    with multiprocessing.Pool(processes=5) as threads:
        threads.map(processa, parametros)


if __name__ == '__main__':
    main()