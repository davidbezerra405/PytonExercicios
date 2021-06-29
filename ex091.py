from random import randint
from time import sleep
jogadas = dict()
jogord = dict()
cont = 1
print('Valores sorteados:')
for j in range(1, 5):
    jogadas['jogador'+str(j)] = randint(1, 6)
    print(' '*2, f'O {"jogador"+str(j)} tirou {jogadas["jogador"+str(j)]}')
    sleep(1)

print('\nClassificando', end='')
for i in sorted(jogadas, key=jogadas.get, reverse=True):
    jogord[i] = jogadas[i]
    print('.', end='')
    sleep(1)

print('\n\nRanking dos jogadores:')
for k, v in jogord.items():
    print(' '*2, f'{cont}º - {k} com {v} pontos')
    cont += 1
    sleep(1)
print('\nfim')
