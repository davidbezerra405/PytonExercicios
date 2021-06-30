from re import match

def leiaFloat(msg='Digite um número: '):
    while True:
        num = str(input(msg)).strip()
        if num.isdecimal():
            break
        print('\033[0;31mERRO! Digite um número com decimal válido.\033[m')
    return int(num)


def leiaInt(msg='Digite um número: '):
    while True:
        num = str(input(msg)).strip()
        if num.isnumeric():
            break
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return int(num)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
