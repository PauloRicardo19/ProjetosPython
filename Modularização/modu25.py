#Calcular tempo de jogo. (SEM PASSAGEM DE PARAMETRO)
HoraInicio: int = 0
MinInicio: int = 0
HoraFim: int = 0
MinFim: int = 0
Fim: int = 0
Inicio: int = 0
Duracao: int = 0

def calc():
    global Inicio
    global HoraInicio
    global MinInicio
    global Fim
    global HoraFim
    global MinFim
    global Duracao
    Inicio = (HoraInicio * 60) + MinInicio
    Fim = (HoraFim * 60) + MinFim
    if Fim < Inicio:
     Fim = Fim + 24 * 60
    Duracao = Fim - Inicio
    Horas = Duracao // 60
    Min = Duracao % 60
    print ('O jogo durou',Horas,':' ,Min)

def main():
    global HoraInicio
    global HoraFim
    global MinFim
    global MinInicio
    HoraInicio = int(input("Hora de inicio? (0 a 23): "))
    MinInicio = int(input("Minuto de inicio? (0 a 59): "))
    HoraFim = int(input("Hora de termino? (0 a 23): "))
    MinFim = int(input("Minuto de termino? (0 a 59): "))
    calc()

if __name__ == '__main__':
    main()

