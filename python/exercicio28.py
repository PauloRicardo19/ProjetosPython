#preço novo de um produto com alguns reajustes

PreçoAtual = float(input("Qual o preço atual do produto? "))
Venda = float(input("Qual a Venda mensal do produto? "))
if Venda < 500 and PreçoAtual < 30.00:
    PreçoNovo = PreçoAtual + (PreçoAtual * 0.10)
elif Venda >= 500 and Venda < 1000 and PreçoAtual >= 30.00 and PreçoAtual < 80.00:
    PreçoNovo = PreçoAtual + (PreçoAtual * 0.15)
elif Venda >= 1000 and PreçoAtual >= 80.00:
    PreçoNovo = PreçoAtual - (PreçoAtual * 0.05)
else:
    PreçoNovo = PreçoAtual
print (PreçoNovo)
     