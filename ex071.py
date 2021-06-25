print('='*40)
print(f'{"BANCO CEV":^40}')
print('='*40)
saque = int(input('Qual valor você quer sacar? R$ '))
cedulas = [100, 50, 20, 10, 5, 1]
cedula = 0
totalcedulas = 0
while True:
    if saque >= cedulas[cedula]:
        saque -= cedulas[cedula]
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'Total de {totalcedulas:2} cédulas de R$ {cedulas[cedula]:3}')
        if saque == 0:
            break
        cedula += 1
        totalcedulas = 0
print('='*40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
