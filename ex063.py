num = int(input('Informe um número inteiro: '))
n1 = 1
nt = 0
elem = 1
print('{}'.format(0), end='')
while elem < num:
    print(' > {}'.format(n1), end='')
    nt2 = n1
    n1 = n1 + nt
    nt = nt2
    elem += 1
print('\nFIM')
