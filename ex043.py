peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)
print('IMC: {:.2f} - '.format(imc), end='')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <= 25.0:
    print('Peso ideal')
elif 25 < imc <= 30:
    print('Sobrepeso')
elif 30 < imc <= 40:
    print('Obsidade')
else:
    print('Obsidade mórbida')

