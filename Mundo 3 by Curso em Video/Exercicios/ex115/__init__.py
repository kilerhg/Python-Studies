# crie um pequeno sistema modularizado que
# permita cadastrar pessoas pelo seu nome e idade em um arquivo de txt simples
# o sistema so vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas
def titulo(texto):
    texto = str(texto)
    print('*-' * 25)
    print(f'{texto.title(): ^50}')
    print('*-' * 25)

def menu():
    titulo('menu primario')
    print(''' 1 - Ver pessoas Que estão cadastradas
 2 - Cadastrar novas Pessoas
 3 - Sair do Programa
    ''')
    while True:
        try:
            escolha = int(input('Escolha uma opção:'))
        except ValueError:
            print('Erro: Digite um valor inteiro Corretamente!!')
        except:
            print('Erro: Desconhecido')
        else:
            if 1 <= escolha <= 3:
                break
            else:
                print(f'A opção "{escolha}" não existe')
    return escolha


def lerNome():
    while True:
        try:
            nome = str(input('Digite o Nome:')).strip().title()
            vazio = nome.split()
            vazio = ''.join(vazio)
        except:
            print('Erro: Desconhecido')
        else:
            if vazio.isalpha() and nome != '':
                break
    return nome


def lerIdade():
    while True:
        try:
            idade = int(input('Digite a Idade:'))
        except ValueError:
            print('Erro: Digite Corretamente uma idade')
        except:
            print('Erro: Desconheido')
        else:
            if idade > 0:
                break
            else:
                print('Idade não pode ser negativa ou igual a 0')
    return idade


def formatarTexto(nome,idade):
    formato = f'{nome[:40]: <42}{idade: >3} Anos'
    return formato


def salvarDados(texto_formatado):
    texto_formatado = str(texto_formatado)
    arquivo = open('base_dados.txt', 'a+')
    arquivo.write(f'{texto_formatado}\n')


def lerDados():
    try:
        arquivo = open('base_dados.txt', 'r+')
    except:
        print('Erro: Salve ao menos 1 registro para abrir')
    else:
        titulo('pessoas no banco de dados')
        print(arquivo.read())
