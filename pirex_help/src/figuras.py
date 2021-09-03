class retangulo():
    
    def __init__(self, centro, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento
        self.centro = centro

    def __str__(self):
        pass

    def calcular_perimetro(self):
        resultado = (self.largura * 2) + (self.comprimento * 2)
        return resultado
    
    def calcular_area(self):
        resultado = self.largura * self.comprimento
        return resultado

class circulo:
    def __init__(self, raio, centro):
        self.centro = centro
        self.raio = raio

    def __str__(self):
        pass

    def calcular_perimetro(self):
        return self.raio * (2 * 3.14)

    def calcular_area(self):
        return 3.14 * ( self.raio ** 2 )