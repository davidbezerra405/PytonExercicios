pessoas = list()
dados = list()
maiorpeso = menorpeso = 0.0
while True:
    print('-'*40)
    print(f'Pessoa: {len(pessoas)+1}')
    dados.append(str(input('Nome: ')).strip().upper())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
for i, p in enumerate(pessoas):
    if i == 0 or maiorpeso < p[1]:
        maiorpeso = p[1]
    if i == 0 or menorpeso > p[1]:
        menorpeso = p[1]
print('-'*40)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorpeso:.1f}Kg. Peso de ', end='')
for pe in pessoas:
    if maiorpeso <= pe[1] <= maiorpeso:
        print(f'[{pe[0]}]', end=' ')
print(f'\nO menor peso foi de {menorpeso:.1f}Kb. Peso de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end=' ')
