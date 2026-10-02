import os 

nome: str = ''
nota1: float  = 0.0 
nota2: float = 0.0 
nota3: float = 0.0 
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''

def escreveArq(caminho, arquivo, linha_arq):
    file: str = ''
    tipo: str = ''
    enc: str = ''
    caminho_completo: str = ''

    enc = 'utf-8'
    caminho_completo = caminho + '/' + arquivo

    if (os.path.exists(caminho) and os.path.isdir(caminho)):
        tipo = 'w'
        if (os.path.exists(caminho_completo)):
            tipo = 'a'
        with open (caminho_completo, tipo, encoding=enc) as file:
            file.write(linha_arq)
    else:
        print ('Diretório inválido. ')        

def cadastro(nm,nt1,nt2,nt3,nt4,vlr_med):
    linha: str = ''
    global arq
    global dir 
    dir = '/tmp/exercicios'
    arq = 'ex21.txt'

    linha = nm + ';' + (str(nt1)) + ';' + (str(nt2)) + ';' + (str(nt3)) + ';' + (str(nt4)) + ';' + (str(vlr_med)) + '\n'

    escreveArq(dir, arq, linha)


def med(n1,n2,n3,n4):
    media: float = 0.0
    media = (n1 + n2 + n3 + n4) / 4
    return media


def entrada():
    global nome 
    global nota1
    global nota2
    global nota3
    global nota4
    global valor_media 

    nome = (input("Digite o nome do aluno: "))
    nota1 = float(input("Qual o valor da primeira nota?: "))
    nota2 = float(input("Qual o valor da segunda nota?: "))
    nota3 = float(input("Qual o valor da terceira nota?: "))
    nota4 = float(input("Qual o valor da quarta nota?: "))

    valor_media = med(nota1,nota2,nota3,nota4)
    print (valor_media)
    cadastro(nome,nota1,nota2,nota3,nota4,valor_media)




def main():
    contador: int = 0
    pasta: str = ''
    pasta = '/tmp/exercicios'
        
    os.mkdir(pasta)
    os.chmod(pasta, 0o744)  

    for contador in range (1,6):
        entrada()




if (__name__ == '__main__'):
    main()