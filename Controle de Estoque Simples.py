print('{:=^40}'.format(' CONTROLE DE ESTOQUE '))
print('cód.234 CALCINHA \ncód.235 SUTIÃ \ncód.236 CONJUNTO \ncód.237 CUECA')
print('-='*20)
quant = calcinha = sutiã = conjunto = cueca = 0
cont = 0
while True:
    quant = int(input('Digite a quantidade: '))
    item = int(input('Digite o código do item: '))
    if item == 234:
        calcinha += quant
        print('Registro realizado com sucesso!')
    elif item == 235:
        sutiã += quant
        print('Registro realizado com sucesso!')
    elif item == 236:
        conjunto += quant
        print('Registro realizado com sucesso!')
    elif item == 237:
        cueca += quant
        print('Registro realizado com sucesso!')
    else:
        print('\033[0;31mCódigo do item incorreto!Tente novamente!')
    print('\033[m{:=^40}'.format(' Novo Registro '))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Registrar mais um produto?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:=^40}'.format(' QUANTIDADE TOTAL NO ESTOQUE '))
print(f'cód.234 CALCINHA ---> {calcinha}')
print(f'cód.235 SUTIÃ    ---> {sutiã}')
print(f'cód.236 CONJUNTO ---> {conjunto}')
print(f'cód.237 CUECA    ---> {cueca}')