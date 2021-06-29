pessoas = list()
pessoa = dict()
mediaidade = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    mediaidade += pessoa['idade']
    pessoas.append(pessoa.copy())
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('-'*40)
print(f'- O grupo tem {len(pessoas)} pessoas.')
mediaidade = (mediaidade / len(pessoas))
print(f'- A média de idade é de {mediaidade:.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for g in pessoas:
    if g['sexo'] == 'F':
        print(g['nome'], end=' ')
print('\n- Lista das pessoas que estão acima da média:')
for g in pessoas:
    if g['idade'] >= mediaidade:
        print(' ' * 2, end='')
        for k, v in g.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
