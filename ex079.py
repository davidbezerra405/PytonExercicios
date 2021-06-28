valores = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if op == 'N':
        break
valores.sort()
print('-'*40)
print(f'Voce digitou os valores {valores}')
