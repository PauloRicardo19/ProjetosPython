#receber o ano de nascimento e o ano atual, calcular a idade e mostrar quantos tera em 17 anos

nascimento = (int(input("Em que ano voce nasceu?: ")))
ano_atual = (int(input("Em que ano estamos?: ")))
idade = ano_atual - nascimento
futuro = idade + 17
print("voce tem:",idade)
print("e em 17 anos vai ter:",futuro)