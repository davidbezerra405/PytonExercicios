from random import randint
vitorias = 0
parimpar = ('P', 'I')
print('#'*40)
print(f'{"VAMOS JOGAR PAR OU ÍMPAR":^40}')
print('#'*40)
while True:
    numcomp = randint(0, 5)
    numjogador = int(input('Escolha um número de 0 a 5: '))
    opjogador = ' '
    while opjogador not in 'PI':
        opjogador = str(input('Escolha (P) para PAR ou (I) para ÍMPAR: ')).strip().upper()[0]
    resultado = parimpar[((numcomp + numjogador) % 2)]
    print('-'*40)
    print(f'O computador escolheu {numcomp}')
    print(f'Você escolheu {numjogador}')
    print(f'Total da rodada = {numcomp+numjogador} ', end='')
    if resultado == 'P':
        print('(PAR)')
    else:
        print('(ÍMPAR)')
    if resultado == opjogador:
        print('Você VENCEU!')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break
    print('Vamos jogar novamente...')
    print('-'*40)
print('='*40)
print(f'GAME OVER! Você venceu {vitorias} vez(es)')
