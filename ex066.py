print(f'{" Exercício 66 ":=^20}')
s = q = 0
while True:
    num = int(input(f'Digite {q+1:>2}º número inteiro (999=parar): '))
    if num == 999:
        break
    s += num
    q += 1
print(f'A soma dos {q} números foi {s}!')
