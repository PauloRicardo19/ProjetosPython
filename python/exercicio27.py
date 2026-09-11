#Velocidade media

voltas = int(input("Quantas voltas? "))
extensao = float(input("Qual a extensao do circuito em METROS? "))
tempo = float(input("QUal a duraçao em MINUTOS? "))
Distancia = voltas * extensao
Distancia = Distancia / 1000
Horas = tempo / 60
Velocidade = Distancia / Horas
print (Velocidade,"Km/h")
