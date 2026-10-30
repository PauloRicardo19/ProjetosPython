import multiprocessing 
import time
import random

def Corrida(sapos):
    salto: int = 0
    distancia: int = 0
    while distancia < 50:
        salto = random.randint(1,5)
        print (sapos,"Saltou",salto,'cm')
        distancia = distancia + salto
        print (sapos,"Percorreu",distancia,'cm')
    print ('#',sapos,'venceu')
        
def main():
    identificador: int = 0
    contador: int = 0
    Sapos: int = [0]*5
    for contador in range (0,5,1):
        identificador = contador + 1
        Sapos[contador] = identificador 
    
    
    with multiprocessing.Pool(processes=5) as threads:
       threads.map(Corrida, Sapos)
    

if __name__ == '__main__':
    main()