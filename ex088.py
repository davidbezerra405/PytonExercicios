from random import randint
from time import sleep
jogo = list()
print('-'*40)
print(f'{"JOGO DA MEGA SENA":^40}')
print('-'*40)
qnt = int(input('Quantos jogos você quer que eu sorteie? '))
for j in range(0, qnt):
    jogo.append([])
    while True:
        num = randint(1, 60)
        if num not in jogo[j]:
            jogo[j].append(num)
        if len(jogo[j]) == 6:
            break
for p, j in enumerate(jogo):
    j.sort()
    print(f'Jogo {p+1:>2}: {j}')
    sleep(1)
print(f'{"< BOA SORTE! >":-^40}')
