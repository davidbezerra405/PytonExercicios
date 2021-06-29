jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(0, partidas):
    gols.append(int(input(f'   Quantos gols na partida {p+1}: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-'*56)
print(jogador)
print(('-'*56))
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*56)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for p, v in enumerate(jogador['gols']):
    print(' '*3,f'=> Na partida {p+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
