jogadores = list()
jogador = dict()
gols = list()
while True:
    print('-'*31)
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    totalgols = 0
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
        totalgols += gols[p]
    jogador['gols'] = gols[:]
    jogador['total'] = totalgols
    gols.clear()
    jogadores.append(jogador.copy())
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('-'*37)
print(f'{"Cod":<3} {"nome":<10} {"gols":<15} {"total":^5}')
print('-'*37)
for c, l in enumerate(jogadores):
    print(f'{c:>3} {l["nome"]:<10} {str(l["gols"]):<15} {l["total"]:>5}')
print('-'*37)
while True:
    op = int(input('Mostrar dados de qual jogador? '))
    if op == 999:
        break
    if 0 <= op <= len(jogadores)-1:
        print(f'-- Levantamento do jogador {jogadores[op]["nome"]}:')
        for j, g in enumerate(jogadores[op]['gols']):
            print(' '*2, f'No jogo {j+1} fez {g} gols.')
        print('-'*40)
    else:
        print(f'ERRO! Não existe jogador com o código {op}! Tente novamente')
print('>> FIM <<')
