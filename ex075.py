lista = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print(f'Você digitou os valores {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
if lista.count(3) == 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {lista.index(3)+1}ª posição')
print('Os valores pares digitados foram ', end='')
qnt = 0
for num in lista:
    if (num % 2) == 0:
        print(num, end=' ')
        qnt += 1
if qnt == 0:
    print('nenhum')
print('')
