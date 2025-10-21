from exer109 import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco,True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco,True)}')
print(f'Atribuindo 10% ao valor fica {moeda.aumentar(preco, 10, True)}')


