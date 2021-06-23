opcoes = '[1]somar\n[2]miltiplicar\n[3]maior\n[4]novos números\n[5]sair do programa'
op = 0
while op != 5:
    num1 = int(input('Informe o 1º número: '))
    num2 = int(input('Informe o 2º número: '))
    print('')
    op = 0
    while op not in [4, 5]:
        print(opcoes)
        op = int(input('Escolha: '))
        if op == 1:
            print('\nSoma: {} + {} = {}\n'.format(num1, num2, num1+num2))
        elif op == 2:
            print('\nMultiplicação: {} x {} = {}\n'.format(num1, num2, num1 * num2))
        elif op == 3:
            maior = num1
            if num2 > maior:
                maior = num2
            print('\nMaior: {} é o maior número.\n'.format(maior))
        elif op not in [4, 5]:
            print('\n OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')
print('FIM')
