
def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except  FileNotFoundError:
        return  False
    else:
        return True

def criarArquivo(nome):
    try:
        a  = open(nome,'wt+')
        a.close()
    except:
        print('houve um erro bna criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
def lerArquivo(arq):
    try:
        a =  open(arq,'rt')
    except:
        print('ERRO! AO LER ARQUIVO')
    else:
        cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dado =  linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()

def cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq,'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} Adicionado')
        a.close()