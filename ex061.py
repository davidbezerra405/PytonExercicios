a1 = int(input('Informe o 1º termo da PA: '))
rz = int(input('Informe a razão da PA: '))
termo = 1
while termo <= 10:
    print('{:3}, '.format(a1), end='')
    a1 += rz
    termo += 1
print('')
print('fim')
