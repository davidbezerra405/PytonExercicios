num = int(input('Informe um valor inteiro: '))
print('Base para conversão:')
print('1-binário\n2-octal\n3-hexadecimal')
op = int(input('Escolha: '))
if op == 1:
    print('binário: {0:b}'.format(num))
elif op == 2:
    print('octal: {0:o}'.format(num))
elif op == 3:
    print('hexadecimal: {0:x}'.format(num))
else:
    print('Opção inválida!')
