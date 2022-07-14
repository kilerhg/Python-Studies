# dentro do pacote UtilidadesCeV que criamos no desafio 111 temos um modulo chamado dado, crie uma função chamada
# leiaDinhiro()e que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetarios
# realizando calculo com ,
# 

from ex112.utilidadesCev.moeda import *
from ex112.utilidadesCev.dado import *

n1 = leiaDinheiro()
n2 = float(input('Digite as Porcentagens:'))
resumo(n1,n2,True)