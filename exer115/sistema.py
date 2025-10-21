from exer115.blibi.interface import *
from exer115.blibi.arquivo import *

arq = 'guanabara.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar uma pessoa', 'Sair do programa'])
    if resp == 1:
        #lista com as pessoas cadastradas
        lerArquivo(arq)
    elif resp == 2:
        #adiciona uma nova pessoa a lista
        cabecalho('NOVO CADASTRO')
        nome = str(input('Digite o nome: '))
        idade = leiaInt('Digite a idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('\033[0;31mSaindo do sistema...\033[m')
        break
    else:
        print(' \033[0;31mERRO: Digite uma opção valida!\033[m')