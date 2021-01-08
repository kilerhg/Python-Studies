from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, CNPJ, nome, idade):
        super().__init__(nome, idade)
        self.CNPJ = CNPJ

    def getCNPJ(self):
        return self.CNPJ

    def setCNPJ(self, CNPJ):
        self.CNPJ = CNPJ