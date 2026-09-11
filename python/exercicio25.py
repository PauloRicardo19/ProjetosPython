#receba a hora de inicio e final de um jogo, calcular o tempo em minutos sabendo que pode começar num dia e terminar noutro

HoraInicio = int(input("Hora de inicio? (0 a 23): "))
MinInicio = int(input("Minuto de inicio? (0 a 59): "))
HoraFim = int(input("Hora de termino? (0 a 23): "))
MinFim = int(input("Minuto de termino? (0 a 59): "))
Fim: int = 0
Inicio: int = 0
#Transforma tudo em minutos
Inicio = (HoraInicio * 60) + MinInicio
Fim = (HoraFim * 60) + MinFim
#verifica se terminou no dia seguinte
if Fim < Inicio:
    Fim = Fim + 24 * 60 
Duracao = Fim - Inicio
Horas = Duracao // 60
Min = Duracao % 60
print (Horas,"Horas e",Min,"Minutos")
