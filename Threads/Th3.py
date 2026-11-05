import multiprocessing 
import time
import random
semaforo: None
podium: None

def init(S,P):
    global semaforo
    global podium
    semaforo = S
    podium = P

def chegada (Frogs):
    global semaforo
    global podium
    
    podium.value = podium.value + 1
    print (Frogs,'Chegou em:',podium.value,'o')

def Corrida(sapos):
    global semaforo
    global podium
    salto: int = 0
    distancia: int = 0
    cont: int = 1
    while distancia < 50:
        salto = random.randint(1,5)
        print (sapos,"Saltou",salto,'cm')
        distancia = distancia + salto
        print (sapos,"Percorreu",distancia,'cm')
      
    with semaforo:
        chegada(sapos)
        
def main():
    sema: int = 0
    podi: int = 0
    identificador: int = 0
    contador: int = 0
    Sapos: int = [0]*5
    for contador in range (0,5,1):
        identificador = contador + 1
        Sapos[contador] = identificador 

    podi = multiprocessing.Value('i',0)    
    sema = multiprocessing.Value('i',0)    
    
    with multiprocessing.Manager() as gerenciador:
        sema = gerenciador.Semaphore(1)
        with multiprocessing.Pool(processes=5, initializer=init, initargs=(sema, podi, )) as threads:
            threads.map(Corrida, Sapos)
    

if __name__ == '__main__':
    main()
