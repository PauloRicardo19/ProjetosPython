import os
valor: int = 0
dir: str = ''
arq: str = ''
arq: str = ''

def mult(vlr,tab):
    res = vlr * tab
    return res
    

def grava(c,rslt):
    global dir  
    global arq
    dir = '/tmp/exercicios'
    arq = 'ex34.txt'
    file: str = ''
    tipo: str = '' 
    enc: str = ''
    linha: str = ''

    enc = 'utf-8'
    linha = (str(rslt)) + '\n'
    caminho = dir + '/' + arq 

    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        if c >0:
            if (os.path.exists(caminho)):
                tipo = 'a'
        with open (caminho, tipo, encoding=enc) as file:
            file.write(linha)
    else: 
        print ("Diretório inválido. ")
                    
        
        

def main():
    pasta: str = ''
    pasta = '/tmp/exercicios'
    
    os.mkdir(pasta)
    os.chmod(pasta, 0o744)    

    global valor
    contador: int = 1
    result: int = 0

    valor = int(input('Digite um valor entre 1-10: '))
    if valor >=1 and valor <=10:
        for contador in range (1, 11):
            result = mult(valor, contador)
            grava(contador, result)
    
    
if __name__ == '__main__':
    main()