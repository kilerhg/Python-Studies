# Criar uma classe que receba o nome do jogo, preço, Data lançamento, Analises steam recentes, Genero

class Jogo:
    def __init__(self, nome, preco, lancamento, analises, genero):
        self.nome = nome
        self.preco = preco
        self.lancamento = lancamento
        self.analises = analises
        self.genero = genero

    def Executar(self):
        print(f'Abrindo o Jogo {self.nome}')

    def Fechar(self):
        print(f'Fechando o Jogo {self.nome}')

    def Avaliar(self):
        avalir_jogo = str(input('Avalie o Jogo:')).strip

    def ExibirInformacoesJogo(self):
        print(self.nome, self.preco, self.lancamento, self.analises, self.genero)

game = Jogo('Europa Universalis IV','17,49','13/ago/2013','Muito Positivas', 'Simulação')

game.ExibirInformacoesJogo()
