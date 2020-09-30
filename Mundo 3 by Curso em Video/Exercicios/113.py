# rescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um numero de tipo invalido aproveite e crie tambem uma função leiafloat() com a mesma funcionalidade
# com keyboard interrumpt

def leiaint():
    while True:
        try:
            valor = int(input('Digite um valor Inteiro:'))
        except KeyboardInterrupt:
            print(f'O Usuario decidiu sair sem digitar valor')
            valor = 0
        except ValueError:
            print('Erro: Digite um numero inteiro Corretamente')
        except:
            print('Erro: Desconhecido')
        else:
            break
    return valor


def leiafloat():
    while True:
        try:
            valor = float(input('Digite um valor Real:'))
        except KeyboardInterrupt:
            print('O usuario decidiu sair sem digitar valor')
            valor = 0
        except ValueError:
            print('Erro: Digite um numero Real Corretamente')
        except:
            print('Erro: Desconhecido')
        else:
            break
    return valor


# Programa Principal
inteiro = leiaint()
decimal = leiafloat()

print(f'O valor inteiro digitado tem valor igual á: {inteiro} e o real: {decimal}')

