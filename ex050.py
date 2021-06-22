soma = 0
for c in range(0, 6):
    num = int(input('Informe {}º número inteiro: '.format(c+1)))
    if (num % 2) == 0:
        soma += num
print('Soma dos número pares: {}'.format(soma))
