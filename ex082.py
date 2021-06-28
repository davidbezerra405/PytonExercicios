lista = list()
listapar = list()
listaimpar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
for n in lista:
    if (n % 2) == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
