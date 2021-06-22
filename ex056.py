somaidade = 0
idadevelho = 0
nomevelho = ''
fmenos20 = 0
for c in range(0, 4):
    print('dados da {}ª pessoa:'.format(c+1))
    nome = str(input('Informe o nome: ')).strip()
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo: (M/F) ')).strip().upper()
    print('')
    somaidade += idade
    if sexo == 'M' and idadevelho < idade:
        idadevelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        fmenos20 += 1
print('A média de idade do grupo é: {} anos'.format(somaidade / 4))
if nomevelho == '':
    print('Não há homens no grupo')
else:
    print('O nome do Homem mais velho é: {}'.format(nomevelho))
if fmenos20 == 0:
    print('Não existe mulheres menor de 20 anos no grupo')
else:
    print('No grupo existem {} mulher(es) menor(es) de 20 anos'.format(fmenos20))
