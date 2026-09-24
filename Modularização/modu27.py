#calcular e mostrar velocidade media em km/h com passagem de parametros


def Velocidade_Média(v ,e ,t ):
    distancia: float = 0.0
    velo: float = 0.0
    Horas: float = 0.0
    distancia = v * e
    distancia = distancia / 1000
    Horas = t / 60
    velo = distancia / Horas
    return velo

def main():
    voltas: int = 0
    extensão: float = 0.0
    tempo: float = 0.0
    velo = Velocidade_Média(voltas,extensão, tempo)
    voltas = int(input("Insira a quantidade de voltas: "))
    extensão = float(input("Insira a extensão da pista: "))
    tempo = float(input("Insira a duração em MINUTOS: "))
    Velocidade_Média(voltas, extensão, tempo)
    print (velo,'km/h') 
    

if __name__ == '__main__':
    main()
