#salario a receber com aumentos

horas = float(input("Quantas Horas trabalhadas?: "))
valorhora = float(input("Qual o valor por Horas?: "))
porcentualdesconto = float(input("Qual o porcentual de desconto?: "))
dependentes = int(input("Quantos Dependentes?: "))

salariobruto = horas * valorhora
valordesconto = salariobruto * (porcentualdesconto / 100)
salarioliquido = salariobruto - valordesconto
salariofinal = salarioliquido + (dependentes * 100)
print("Salario a receber em R$:",salariofinal)