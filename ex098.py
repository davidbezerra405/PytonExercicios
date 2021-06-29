from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    print('-'*40)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        fim -= 1
        if passo > 0:
            passo *= -1
    if inicio < fim:
        fim += 1
    for c in range(inicio, fim, passo):
        print(f'{c} ', end='', flush=True)
        sleep(0.5)
    print(' FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('-'*40)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
