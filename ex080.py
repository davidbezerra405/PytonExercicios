num = list()
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    adpos = -1
    for p, nl in enumerate(num):
        if nl > n:
            num.insert(p, n)
            adpos = p
            break
    if adpos == -1:
        num.append(n)
        print('Adicionado no final da lista...')
    else:
        print(f'Adicionado na posição {num.index(n)} da lista...')
print(f'Os valors digitados em ordem foram {num}\n')