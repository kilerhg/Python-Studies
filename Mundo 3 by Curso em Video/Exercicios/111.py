# crie um pacote chamado utilidadesCeV que tenha dois modulos internos chamados moeda e dado.
# transfira todas as funções utilizadas nos desafios 107 ate o 110 para o primeiro
# pacote e mantenha tudo funcionando

from ex111.utilidadesCev.moeda import *
from ex111.utilidadesCev.dado import *

n1 = float(input('Digite um Valor:'))
n2 = float(input('Digite as Porcentagens:'))
resumo(n1,n2,True)
