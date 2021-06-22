from datetime import datetime
anoatual = datetime.now().year
maior = 0
menor = 0
for c in range(0, 7):
    anonasc = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c+1)))
    if (anoatual - anonasc) < 21:
        menor += 1
    else:
        maior += 1
print('{} pessoa(s) são menor de 21 anos'.format(menor))
print('{} pessoa(s) são tem de 21 anos acima.'.format(maior))
