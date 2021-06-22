num = int(input('Informe o valor de 1 a 10 para gerar a tabuada: '))
if 1 <= num <= 10:
    print('Tabuada do {}'.format(num))
    for c in range(1, 11):
        print('{:2} x {:2} = {:3}'.format(c, num, c * num))
else:
    print('Valor inválido!')
