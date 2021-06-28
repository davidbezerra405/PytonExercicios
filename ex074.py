from random import randint
lista = (randint(1, 9), randint(1, 9), randint(1, 9),
          randint(1, 9), randint(1, 9))
print('Lista de números gerados: ', end='')
for num in lista:
    print(num, end=' ')
print(f'\nO menor número foi {min(lista)}')
print(f'O maior número foi {max(lista)}')
