while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 40)
    for t in range(1, 11):
        print(f'{num} x {t:>2} = {num*t:>4}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
