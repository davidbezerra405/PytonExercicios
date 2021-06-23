from random import randint
jogar = 'S'
while jogar == 'S':
    print("="*50)
    print("{:50}".format('Jogo da Adivinhação'))
    print("="*50)
    numcomp = randint(0, 10)
    numjog = -1
    tentativas = 0;
    print('Adivinhe o número de 0 a 10: ')
    while numcomp != numjog:
        tentativas += 1
        numjog = int(input('--> Tentativa {}: '.format(tentativas)))
        if numjog < 0 or numjog > 10:
            print('\nEscolha de 0 até 10 meu jovem.\nTente novamente.\n')
        elif numcomp != numjog:
            print('Você errou!')
            if numcomp > numjog:
                print('o número esta menor,')
            else:
                print('o número esta maior,')
            print('Tente novamente!')
    print('\nO computador escolheu {}, você acertou após {} tentativa(s)\n'.format(numcomp, tentativas))
    jogar = str(input('Quer jogar novamente [S=sim] ')).strip().upper()
print('Fim do jogo...')
