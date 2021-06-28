lista = [[], []]
for i in range(0, 7):
    v = int(input(f'Digite o {i+1}º valor: '))
    lista[v % 2].append(v)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
