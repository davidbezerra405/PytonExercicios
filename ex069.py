qnt = qntmais18 = qntmasc = qntfemmenos20 = 0
while True:
    print('-'*40)
    desc = f'CADASTRE A {qnt+1}º PESSOA'
    print(f'{desc:^40}')
    print('-'*40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        qntmasc += 1
    elif (sexo == 'F') and (idade < 20):
            qntfemmenos20 += 1
    if idade >= 18:
        qntmais18 += 1
    qnt += 1
    print('-'*40)
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
    if op == 'N':
        break
print(f'{" FIM DO PROGRAMA ":=^40}')
print(f'Total de pessoas com mais de 18 anos: {qntmais18}')
print(f'Ao todo temos {qntmasc} homen(s) cadastrado(s)')
print(f'E temos {qntfemmenos20} mulher(es) com menos de 20 anos')
