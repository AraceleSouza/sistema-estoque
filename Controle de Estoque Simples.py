print('{:=^40}'.format(' CONTROLE DE ESTOQUE '))

produtos = {}

while True:
    nome = input('Nome do produto: ').strip().lower()
    quantidade = int(input('Quantidade: '))

    if nome in produtos:
        produtos[nome] += quantidade
    else:
        produtos[nome] = quantidade

    print('Registro realizado com sucesso!')

    resp = input('Registrar mais um produto? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('{:=^40}'.format(' ESTOQUE FINAL '))

for produto, qtd in produtos.items():
    print(f'{produto.upper():<20} ---> {qtd}')
