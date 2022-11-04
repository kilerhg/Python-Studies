from codigo.bytebank import Funcionario
import pytest
from pytest import mark

def sum_num(a,b):
    return a+b

class TestClass:
    def test_quando_idade_recebe_13_03_200_deve_retornar_22(self):
        
        entry = '13/03/2000' # Given-Contexto
        expected = 22

        func = Funcionario('teste', entry, 1111)
        
        result = func.idade() # When-Ação

        assert result == expected # Then-Desfecho
    
    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self):
        entry = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'
        lucas = Funcionario(entry, '11/11/2000', 1111)
        result = lucas.sobrenome()
        assert result == esperado
    
    #@mark.skip
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 # Given
        entrada_nome = 'Paulo Bragança' # Given
        esperado = 90000 

        func = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

        func.decrescimo_salario() # when

        resultado = func.salario 

        assert resultado == esperado # Then
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entry = 1000 # Given
        esperado = 100
        lucas = Funcionario('teste', '11/11/2000', entry)
        result = lucas.calcular_bonus()
        assert result == esperado
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entry = 1000000 # Given
            lucas = Funcionario('teste', '11/11/2000', entry)
            result = lucas.calcular_bonus()
            assert result
    
    def test_when_sum_receive_1_1_should_return_2(self):
        entry1 = 1 # Given-Arrange
        entry2 = 1 # Given-Arrange
        expect = 2

        result = sum_num(entry1, entry2) # When-Action

        assert result == expect # Then-Assert

    def test_when_str_return_self(self):
        name, birthday, salario = 'Teste', '12/03/2000', 1000
        expected = 'Funcionario(Teste, 12/03/2000, 1000)'

        func = Funcionario(name, birthday, salario)
        result = func.__str__() # When

        assert result == expected # Then-Assert

        