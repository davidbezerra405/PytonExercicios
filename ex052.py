num = int(input('Informe um número: '))
primo = 1 # 1 = primo
for c in range(2, num):
    if (num % c) == 0:
        primo = 0 # 0 = não primo
if primo == 0:
    print('Não é número primo!')
else:
    print('É número primo')
