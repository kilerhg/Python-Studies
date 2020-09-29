# funcao chamada notas que pode receber varias notas de alunos e vai
# retornar um dicionario com as seguintes informacoes:
# quantidade de notas
# A maior nota
# A menor nota
# a media da turma
# a situação (opcional) ruim(media<5), razoavel(5<media<7), boa(7<media)
# adicione uma docstring

def notas(*notas,situ=False):
    """
        -> Função Para calcular media e Verificar Situação
    :param notas: Valores Decimais
    :param situ: Se deseja mostrar a situação, True / False
    :return: dicionario com as maximas e minimas e situação caso situ = True
    """

    dc = {}
    ls = notas
    '''
    Codigo Redundante pois o '* notas' ja cria um lista com os elementos digitados
    
    ls = []
    for x in notas:
        ls.append(x)
        '''
    dc['Total'] = len(ls)
    dc['Maior'] = max(ls)
    dc['Menor'] = min(ls)
    dc['Media'] = sum(ls) / len(ls)
    if situ:
        if dc['Media'] < 5:
            dc['Situação'] = 'Ruim'
        elif 5 <= dc['Media'] < 7:
            dc['Situação'] = 'Razoavel'
        else:
            dc['Situação'] = 'Boa'
    return dc


# Programa Principal
print(notas(5.5, 2.5, 1.5,situ=True))


