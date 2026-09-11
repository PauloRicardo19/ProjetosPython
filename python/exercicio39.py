#quanidade de graos contidos num tabuleiro de xadrez
# CASA = 1,2,3,4.....64
# QTDE = 1,2,4,8..... N 
casa: int = 1
graos: int = 1
i: int = 0
while casa <= 64:
    i = i + graos
    graos = graos * 2
    casa = casa + 1
print ("A quantidade total de graos e:",i)
