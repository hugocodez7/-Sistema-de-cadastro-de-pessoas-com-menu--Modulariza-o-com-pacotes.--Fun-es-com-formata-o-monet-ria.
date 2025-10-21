def leiaInt(a):
    while True:
        try:
            b = int(input(a))
        except (TypeError, ValueError):
            print('\033[0;31mErro! Digite apenas numero valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mPreferiu não informar algum valor!.\033[m')
            return 0
        else:
            return b


def linha(tam=40):
    return '=' * tam


def cabecalho(text):
    print(linha())
    print(text.center(40))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[36m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[37mSua opção: \033[m')
    return opc





