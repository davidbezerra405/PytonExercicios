soma = 0
quant = 0
num = 0
while num != 999:
    num = int(input('Informe o {}º número inteiro: (999=sair) '.format(quant+1)))
    if num != 999:
        quant += 1
        soma += num
print('\nForam digitados {} números.'.format(quant))
print('A soma entre eles foi: {}'.format(soma))
print('FIM')
