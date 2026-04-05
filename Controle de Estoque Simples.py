print('{:=^40}'.format(' CONTROLE DE ESTOQUE '))

produtos = {}

for nome, dados in produtos.items():
    if dados["quantidade"] < dados["minimo"]:
        print(f'{nome} está com estoque baixo!')

while True:
    nome = input('Nome do produto: ').strip().lower()
    quantidade = int(input('Quantidade: '))

    if nome in produtos:
        produtos[nome][quantidade] += quantidade
    else:
        preco = float(input('Preço: '))
        minimo = int(input('Estoque mínimo: '))

        produtos[nome] = {
            "quantidade": quantidade,
            "preco": preco,
            "minimo": minimo
        }

    print('Registro realizado com sucesso!')

    resp = input('Registrar mais um produto? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('{:=^40}'.format(' ESTOQUE FINAL '))

for nome, dados in produtos.items():
    print(f'{nome.upper():<15} | Qtd: {dados["quantidade"]} | Preço: {dados["preco"]}')
