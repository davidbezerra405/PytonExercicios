num = int(input('Informe um número: '))
soma = num
print('{}! = '.format(num), end='')
while num > 1:
    print('{} x '.format(num), end='')
    num -= 1
    soma = soma * num
print('{} = {}'.format(num, soma))
