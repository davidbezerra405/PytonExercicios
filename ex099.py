from time import sleep

def maior(*valores):
    print('-' * 40)
    print('Analizando valores passados...')
    if len(valores) > 0:
        for p, v in enumerate(valores):
            print(f'{v} ', end='', flush=True)
            sleep(0.5)
        print(f'Foram informados {len(valores)} valores ao todo.')
        print(f'O maior valor informado foi {max(valores)}')
    else:
        print('Não foi informado nenhum valor.')


maior([2, 9, 4, 5, 7, 1])
maior([4, 7, 0])
maior([1, 2])
maior([6])
maior()
