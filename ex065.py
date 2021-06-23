soma = 0
maior = 0
menor = 0
quant = 0
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite o {}º número inteiro: '.format(quant+1)))
    soma += num
    if quant == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    quant += 1
    continuar = str(input('Deseja continuar? (S=sim) ')).strip().upper()[0]
print('Foram digitados {} números: '.format(quant))
print('A soma dos número digitados foi: {}'.format(soma))
print('A média dos número digitados foi: {}'.format(soma/quant))
print('O Menor número foi: {} '.format(menor))
print('O maior número foi: {} '.format(maior))
print('\nFIM')
