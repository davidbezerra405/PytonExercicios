r1 = float(input('Informe o valor de R1: '))
r2 = float(input('Informe o valor de R2: '))
r3 = float(input('Informe o valor de R3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('podem formar um triângulo!')
else:
    print('NÃO podem formar um triângulo')
