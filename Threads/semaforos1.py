import multiprocessing
import random
import time

sentido: None
semaforo: None

def init (sema, sent):
    global sentido
    global semaforo
    sentido = sent
    semaforo = sema

def direção(C):
    global sentido
    global semaforo
    sentido.value = C
    if sentido.value == 1:
        print ('O: #',C,'Carro, seguiu para o Norte')
    elif sentido.value == 2:
        print ('O: #',C,'Carro, seguiu para o Sul')
    elif sentido.value == 3:    
        print ('O: #',C,'Carro, seguiu para o Leste')
    else:
        print ('O: #',C,'Carro, seguiu para o Oeste')



def cruzamento (Carro):
    global sentido
    global semaforo
    print ("O Carro: #",Carro,'Chegou ao cruzamento')
    time.sleep(0.05)
    with semaforo:
        direção(Carro)

def main():
    senti: int = 0
    semaf: int = 0
    carros: int = [0]*4
    identificador: int = 0
    i: int = 0
    for i in range (0,4,1):
        identificador = i + 1
        carros[i] = identificador 

    senti = multiprocessing.Value('i',0)    
    semaf = multiprocessing.Value('i',0) 

    with multiprocessing.Manager() as gerenciador:
            semaf = gerenciador.Semaphore(1)
            with multiprocessing.Pool(processes=4, initializer=init, initargs=(semaf, senti, )) as threads:
                threads.map(cruzamento, carros)
        


if __name__ == '__main__':
    main()