a1 = int(input('Informe o 1º termo da PA: '))
rz = int(input('Informe a razão da PA: '))
termo = 0
contador = 1
mostrar = 10
while contador <= mostrar:
    print('{:3}, '.format(a1), end='')
    a1 += rz
    termo += 1
    contador += 1
    if contador > mostrar:
        print('')
        mostrar = int(input('Deseja mostrar mais quantos termos? (0=sair) '))
        contador = 1
print('\nForam mostrados {} termos.'.format(termo))
print('fim')
