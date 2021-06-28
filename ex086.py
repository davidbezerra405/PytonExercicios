lista = [[], [], [], []]
for l in range(0, 4):
    for c in range(0, 4):
        lista[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
for l in lista:
    for c in l:
        print(f'[ {c:>3} ]', end='')
    print()
