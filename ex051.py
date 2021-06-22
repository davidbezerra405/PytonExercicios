a1 = int(input('Informe o 1º termo da PA: '))
rz = int(input('Informe a razão da PA: '))
decimo = a1 + (10 -1) * rz
for c in range(a1, decimo+rz, rz):
    print('{:3}, '.format(c), end='')
print('')
print('fim')
