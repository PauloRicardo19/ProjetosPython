#quatro notas bimestrais e mostrar respostas variaveis
Nota1 = float(input("Qual o valor da primeira nota? "))
Nota2 = float(input("Qual o valor da segunda nota? "))
Nota3 = float(input("Qual o valor da terceira nota? "))
Nota4 = float(input("Qual o valor da quarta nota? "))
MediaArit = (Nota1 + Nota2 + Nota3 + Nota4) / 4
print ("A Media Aritmetica e:",MediaArit)
if MediaArit >= 6.0:
    print ("APROVADO")
elif MediaArit >= 3.0 and MediaArit < 6.0:
    print ("EXAME")
else: 
    print ("RETIDO")