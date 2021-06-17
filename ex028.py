from random import randint
from time import sleep
s = randint(0, 5)
a = int(input('Escolha um número entre 0 e 5: '))
print('Pensando...')
sleep(3)
if s == a:
    print('Parabén! você venceu!')
else:
    print('Que pena, você errou.')
print('número sorteado: {}'.format(s))
