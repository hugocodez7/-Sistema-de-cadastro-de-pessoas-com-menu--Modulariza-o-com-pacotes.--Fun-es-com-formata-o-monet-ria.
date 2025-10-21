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

