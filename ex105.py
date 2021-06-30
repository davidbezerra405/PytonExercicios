def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indica se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    alunos = dict()
    if len(n) == 0:
        return 'Informe no mínmo uma nota.'
    alunos['total'] = len(n)
    alunos['maior'] = max(n)
    alunos['menor'] = min(n)
    alunos['média'] = (sum(n) / len(n))
    if sit:
        if alunos['média'] >= 9:
            alunos['situação'] = 'ÓTIMA'
        elif 9 > alunos['média'] >= 7:
            alunos['situação'] = 'BOA'
        elif 7 > alunos['média'] >= 5:
            alunos['situação'] = 'RAZOÁVEL'
        else:
            alunos['situação'] = 'RUIM'
    return alunos


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
