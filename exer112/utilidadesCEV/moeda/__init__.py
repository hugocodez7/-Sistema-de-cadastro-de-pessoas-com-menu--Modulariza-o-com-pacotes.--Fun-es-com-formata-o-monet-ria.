def metade(p, formato=False):
    p = p/2
    return p if formato is False else moeda(p)


def dobro(p, formato=False):
    p *= 2
    return p if formato is False else moeda(p)


def aumentar(p, aum=0, formato=False):
    p = p + (p * aum/100)
    return p if formato is False else moeda(p)

def diminuir(p, sub=0, formato=False):
    p = p - (p * sub/100)
    return p if formato is False else moeda(p)

def moeda(p, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.',',')


def resumo(p, taxaum=5, taxred=10):
    print('-' * 30)
    print('DETALHES DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{taxaum}% de aumento: \t{aumentar(p, taxaum, True)} ')
    print(f'{taxred}% de desconto: \t{diminuir(p, taxred, True)} ')
