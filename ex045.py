from random import choice
lista = ['Pedra', 'Papel', 'Tesoura']
comp = choice(lista)
print('Opções:\n1-{}\n2-{}\n3-{}'.format(lista[0], lista[1], lista[2]))
jog = int(input('Escolha: '))
if 1 <= jog <= 3:
    jogador = lista[jog-1]
    print('Computador escolheu: {}'.format(comp))
    print('Você escolheu: {}'.format(jogador))
    if comp == jogador:
        print('Empate')
    elif comp == lista[0]: # Pedra
        if jogador == lista[2]: # Tesoura
            print('O Computador ganhou!')
        else:
            print('Você ganhou!')
    elif comp == lista[2]: # Tesoura
        if jogador == lista[1]: # Papel
            print('O Computador ganhou!')
        else:
            print('Você ganhou!')
    elif comp == lista[1]: # Papel
        if jogador == lista[0]: # Pedra
            print('O Computador ganhou!')
        else:
            print('Você Ganhou!')
else:
    print('Opção invalida')

