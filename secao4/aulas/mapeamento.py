produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 20},
    {'nome': 'p3', 'preco':30},
    {'nome': 'p4', 'preco':40},
    {'nome': 'p5', 'preco':50}
]
novos_prdutos = [
    {**produto, 'preco': produto['preco']*1.05}
    for produto in produtos
]
print(*novos_prdutos, sep='\n')