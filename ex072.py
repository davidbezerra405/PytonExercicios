extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catoze', 'quinze', 'dezesseie', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente... ', end='')
print(f'Você digitou {extenso[num]}')
