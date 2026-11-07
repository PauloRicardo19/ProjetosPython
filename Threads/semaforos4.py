import multiprocessing 
import random 
import time 

Semaforo_cinco_carros_pista: None
Semaforo_sete_Equipes: None


def init(Sema_Cinco, Sema_Equipes):
    global Semaforo_cinco_carros_pista
    global Semaforo_sete_Equipes
    Semaforo_cinco_carros_pista = Sema_Cinco
    Semaforo_sete_Equipes = Sema_Equipes

def pista(Carro,Equip):
    Tempo: int = 0
    Tempo_Aleatorio: int = 0
    for i in range (1,4,1):
        Tempo_Aleatorio = random.randint (1000, 3000)
        Tempo = Tempo_Aleatorio / 1000
        time.sleep(Tempo)
        print ('O Carro: #',Carro,'Da equipe: #',Equip,'Realizou a volta:',i,'em',Tempo,'s')
    
        

def Separar_Equipes(Carros):
    global Semaforo_sete_Equipes
    global Semaforo_cinco_carros_pista
    Equipes:int = 0
    Equipes = ( Carros + 1 ) // 2
    time.sleep (0.05)
    print ("O Carro: #",Carros,"Da Equipe: #",Equipes,'Está esperando.')
    with Semaforo_sete_Equipes[Equipes - 1]:
        with Semaforo_cinco_carros_pista:
            time.sleep (0.05)
            print ("O Carro: #",Carros,"Da Equipe: #",Equipes,'Entrou na pista.')
            pista(Carros,Equipes)


def main():
    SemCinc: int = 0
    SemEqui: int = 0
    Carros_A_Separar: int = [0]*14
    Identificador_Carros: int = 0
    Contador: int = 0
    for Contador in range (0,14,1):
        Identificador_Carros = Contador + 1
        Carros_A_Separar[Contador] = Identificador_Carros

    SemCinc = multiprocessing.Value('i',0)
    SemEqui = multiprocessing.Value('i',0)

    with multiprocessing.Manager() as gerenciador:
        SemCinc = gerenciador.Semaphore(5)
        SemEqui =  [gerenciador.Semaphore(1) for i in range(7)]
        with multiprocessing.Pool(processes=14, initializer=init, initargs=(SemCinc, SemEqui, )) as threads:
            threads.map(Separar_Equipes, Carros_A_Separar)   

if __name__ == "__main__":
    main()    