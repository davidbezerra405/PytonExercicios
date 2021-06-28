boletim = list()
dados = list()
notas = list()
while True:
    print(f'Aluno {len(boletim)+1}: ')
    dados.append(str(input('Nome: ')).strip().capitalize())
    notas.append(float(input('1ª nota: ')))
    notas.append(float(input('2ª nota: ')))
    dados.append(notas[:])
    boletim.append(dados[:])
    notas.clear()
    dados.clear()
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if op == 'N':
        break
print('-'*40)
print(f'{" Boletim ":^40}')
print('-'*40)
print(f'| No. | {"Aluno":<20} | {"Média":^7} |')
print('-'*40)
for n, a in enumerate(boletim):
    print(f'| {n:>3} | {a[0]:<20} | {(a[1][0]+a[1][1])/2:>7.1f} |')
print('-'*40)
print(f'{f"Quantidade de alunos: {len(boletim)}":>39}')
while True:
    aluno = str(input('\nDigite o nome do aluno para consulta [S=sair]: ')).strip().capitalize()
    if aluno.upper() == 'S':
        break
    for a in boletim:
        if aluno in a:
            print(f'Aluno: {a[0]}\n1ª nota: {a[1][0]:>7.1f}\n2ª nota: {a[1][1]:>7.1f}\nMédia: {((a[1][0]+a[1][1])/2):>7.1f}')
print('Programa finalizado!')
