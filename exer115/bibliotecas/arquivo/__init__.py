from ..interface import *


def arquivoExiste(nome):
    try:
        b = open(nome, 'rt')
        b.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        b = open(nome, 'wt+')
        b.close()
    except:
        print('Erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado')


def lerArquivo(nome):
    try:
        b = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(b.read())
    finally:
        b.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        b = open(arq, 'at')
    except:
        print('Erro ao abrir arquivo')
    else:
        try:
            b.write(f'{nome}  {idade} anos\n')
        except:
            print('Erro ao escrever os dados')
        else:
            print(f'O nome {nome} foi adicionado')
            b.close()