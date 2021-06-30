def fatorial(n=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fatorial = 1
    for c in range(n, 0, -1):
        if show:
            if c < n:
                print('x ', end='')
            print(f'{c} ', end='')
        fatorial *= c
    if show:
        print('= ', end='')
    return fatorial


print(fatorial(5))
print(fatorial(5, True))
help(fatorial)
