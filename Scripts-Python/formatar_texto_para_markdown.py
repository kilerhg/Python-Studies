# Este Script servira para Transformar texto normal em texto markdown formatado
# Feito para: Facilitar Criação do Sumario no readme.md no github:
# https://github.com/kilerhg/Python-Studies/blob/master/readme.md

def formatar(texto):
    """
        -> Função Utilizada Para Formatar O texto como Sumario MarkDown
    :param texto: Texto Base
    :return: Texto Formatado
    """
    texto = str(texto).lower().replace('#', '').strip()
    texto_limpo = texto.title()
    separado = texto.split()
    texto = f'* [{texto_limpo}](#{"-".join(separado)})'
    print(texto)
    return texto


def desbugar_unicode(texto):
    """
        -> Substitui alguns caracteres com erro do unicode por utf-8
    :param texto: Texto a ser formatado
    :return: Texto formatado
    """
    texto = str(texto)
    texto = texto.replace('Ã§', 'ç')
    texto = texto.replace('Ãµ', 'õ')
    return texto


def salvar_dados(texto_formatado, nome_arquivo='texto_formatado.txt', subtituir=False):
    """
        -> Função Utilizada Para Salvar os Dados Informados em um arquivo Txt
    :param texto_formatado: Dado a ser salvo
    :param nome_arquivo: Arquivo onde irá ser salvo, OPCIONAL
    :param subtituir: Se ira substituir ou não o conteúdo do arquivo
    :return: Não Retorna Valor
    """
    if subtituir:
        param_substituir = 'w+'
    else:
        param_substituir = 'a+'
    texto_formatado = str(texto_formatado)
    arquivo = open(nome_arquivo, param_substituir, encoding='utf-8')
    arquivo.write(f'{texto_formatado}\n')


def ler_bruto():
    """
        -> Está função lê o arquivo informado e separa o conteudo de interesse , salvando em outro arquivo
    :return: Retorna uma lista com o Conteudo De Interesse
    """
    from random import randint
    flag = randint(1000, 9999)
    lista = []
    try:
        arquivo = open('texto_bruto.txt', 'r+', encoding='utf-8')
    except:
        print('Erro: Arquivo Inexistente, Criando....')
        criar = open('texto_bruto.txt', 'a+', encoding='utf-8')
    else:
        try:
            salvar_dados(f'{str(flag)}', 'texto_bruto.txt')
            cont = 0
            while True:
                linha = arquivo.readline(300).replace('\n', '')
                if str(flag) in linha:
                    break
                print(linha)
                if linha != '':
                    if linha[0] == '#':
                        lista.append(linha)
                        print(linha)
                        cont += 1
        except Exception as erro:
            print(f'Arquivo Vazio, erro com nome {erro.__class__}')
    return lista


def ler_dados():
    """
        -> Está função lê o arquivo informado e formata linha por linha
    :return: Uma lista com os valores Formatados
    """
    lista = []
    try:
        arquivo = open('texto_base.txt', 'r+', encoding='utf-8')
    except:
        print('Erro: Arquivo Inexistente, Criando....')
        open('texto_base.txt', 'a+', encoding='utf-8')
    else:
        # print(arquivo.read())
        try:
            cont = 0
            while True:
                linha = desbugar_unicode(arquivo.readline(100).replace('\n', ''))
                if linha == '':
                    break
                lista.append(linha)
                print(linha)
                cont += 1
        except:
            print('Arquivo Vazio')
        else:
            pass
    return lista


# Programa Principal


dados = ler_bruto()
for x in dados:
    salvar_dados(x, 'texto_base.txt', False)
    print(x)

dados = ler_dados()
for x in dados:
    salvar_dados(formatar(x))
