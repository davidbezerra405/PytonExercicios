sexo = ' '
while sexo not in 'MF':
    sexo = str(input('Informe o sexo: (M/F) ')).strip().upper()[0]
    if sexo == 'M':
        sexod = 'masculino'
    elif sexo == 'F':
        sexod = 'feminino'
    else:
        print('Sexo inválido, tente novamente')
print('Sexo: {}'.format(sexod))