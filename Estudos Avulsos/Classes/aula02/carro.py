'''
Criar a classe carro e definir no minimo 3 propiedades e 3 metodos
'''


class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def Ligar_motor(self):
        print(f'O {self.modelo} está ligando o motor')

    def Desligar_motor(self):
        print(f'O {self.modelo} está desligando o motor')

    def Fechar_vidro(self):
        print('Fechando o vidro...')

    def Exibir_info(self):
        print(self.marca, self.modelo, self.ano, self.cor)

carro1 = Carro('Toyota','Corolla','2006','Bege')

carro1.Exibir_info()
