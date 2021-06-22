soma = 0
qnt = 1
print('<'*95)
for c in range(1, 501, 2):
    if (c % 3) == 0:
        soma += c
        qnt += 1
        print('{:3}, '.format(c), end='')
    if (qnt % 20) == 0:
        print('')
        qnt = 1
print('')
print('<'*95)
print('Soma: {}'.format(soma))
