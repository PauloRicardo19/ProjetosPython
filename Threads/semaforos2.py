import multiprocessing
import random 
import time 

port: None

def init(porta):
    global port
    port = porta 

def Porta(P):
    print ("A: #", P, 'Cruzou a porta.')

def corredor(pessoas):
    global port 
    abrir_porta: int = 0
    velocidade: int = 0
    corredor: int = 0
    soma: int = 0
    cruzar_porta: float = 0.0
    print ('A #',pessoas,'Pessoa, chegou ao corredor.')

    corredor = 200
    while soma < corredor:
        time.sleep(0.05)
        velocidade = random.randint (4, 6)
        soma = soma + velocidade
        if soma > corredor: 
            soma = corredor
        print (pessoas,'andou m/s',velocidade)
        print (pessoas,'andou no total m',soma)

    print ('A #', pessoas,'Vai abrir a porta.' )
    abrir_porta = random.randint (1000, 2000)
    cruzar_porta = abrir_porta / 1000
    with port:
        time.sleep(cruzar_porta)
        Porta(pessoas)

def main():
    p: int = 0
    pess: int = [0]*4
    contador: int = 0
    identificador: int = 0
    for contador in range (0,4,1):
        identificador = contador + 1
        pess[contador] = identificador 

    p = multiprocessing.Value('i',0)

    with multiprocessing.Manager() as gerenciador:
        p = gerenciador.Semaphore(1)
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(p, )) as threads:
                        threads.map(corredor, pess)

if __name__ == '__main__':
    main()