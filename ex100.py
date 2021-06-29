from random import randint
from time import sleep
numeros = list()

def somaPar(numeros):
    soma = 0
    for v in numeros:
        if (v % 2) == 0:
            soma += v
    print(f'Somando os valoes pares de {numeros}, temos {soma}')


def sorteia(numeros):
    print('Sorteando 5 valores da lista: ', end='')
    for s in range(0, 5):
        numeros.append(randint(1, 10))
        print(numeros[s], end=' ')
        sleep(1)
    print('PRONTO!')


sorteia(numeros)
somaPar(numeros)
