from datetime import datetime
anonasc = int(input('Ano de nascimento: '))
anoatual = datetime.now().year
idade = anoatual - anonasc
print('Idade: {} '.format(idade))
print('Categoria: ', end='')
if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Junior')
elif 19 < idade <= 20:
    print('Sênior')
else:
    print('Master')
