lista = [[], [], []]
somapar = soma3col = maior2lin = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-'*40)
for pl, l in enumerate(lista):
    for pc, c in enumerate(l):
        print(f'[ {c} ]', end='')
        if (c % 2) == 0:
            somapar += c
        if pc == 2:
            soma3col += c
        if pl == 1 and maior2lin < c:
            maior2lin = c
    print()
print('-'*40)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {soma3col}')
print(f'O maior valor da segunda linha é {maior2lin}')
