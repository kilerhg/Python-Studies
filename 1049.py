'''


Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.
Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada

A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.
Saída

Imprima o nome do animal correspondente à entrada fornecida.

'''

tipo1 = str(input())

if tipo1 == 'vertebrado' :
    tipo2 = str(input())
    if tipo2 == 'ave' :
        tipo3 = str(input())
        if tipo3 == 'carnivoro' :
            print('aguia')
        else :
            print('pomba')
    else :
        tipo3 = str(input())
        if tipo3 == 'onivoro' :
            print('homem')
        else :
            print('vaca')
else :
    tipo2 = str(input())
    if tipo2 == 'inseto' :
        tipo3 = str(input())
        if tipo3 == 'hematofago' :
            print('pulga')
        else :
            print('lagarta')
    else :
        tipo3 = str(input())
        if tipo3 == 'hematofago' :
            print('sanguessuga')
        else :
            print('minhoca')



    