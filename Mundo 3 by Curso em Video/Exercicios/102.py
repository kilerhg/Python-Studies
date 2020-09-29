# uma funcao fatorial que receba dois parametros, o primeiro que indique o numero a calcular
# e o segundo chamado show, que sera um valor logico(opcional) indicando se sera mostrado
# ou nao na tela o processo de calculo do fatorial

def fatorial(num=1,show=False):
    """
        -> Função para calculo de Fatorial
    :param num: Numero a ser calculado / numero inteiro
    :param show: Parametro opcional, se deseja ou não mostrar a conta na tela. True/False
    :return: O resultado do calculo Fatorial
    """
    fac = 1
    if show:
        for x in range(num,0,-1):
            fac *= x
            if x != 1:
                print(f'{x} ',end='x ')
        print(f'{x} = ',end='')
    else:
        for x in range(num,0,-1):
            fac *= x
    return fac


# Programa Principal
print(fatorial(5,True))
