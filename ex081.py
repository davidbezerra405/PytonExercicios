valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista, nas posições: ', end='')
    for p, v in enumerate(valores):
        if v == 5:
            print(p, end='...')
else:
    print('O valor 5 NÃO faz parte da lista!')