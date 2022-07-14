from email_academico import criar_emails_acadamicos
from figuras import retangulo, circulo

def exercício5():

    '''
    Exercício 5
No diretório src crie o módulo util. No módulo util, copie do Tutorial 1 a função
carregar_arquivo_csv e a classe Data, omitindo os métodos que representam os comparadores
relacionais. Adicionalmente no módulo util, implemente a classe descrita a seguir.
classe Endereço
 dados
◦ logradouro, número, complemento, bairro, cidade, estado, cep
 métodos
◦ __init__, __str__
No módulo seguro, implemente a função e as classes descritas a seguir.
obter_população_cidade
 parâmetro
◦ cidade_segurado
 funcionalidade
◦ no diretório dados crie manualmente o arquivo PopulaçõesCidadesBrasileiras.csv com
cidades e populações de algumas cidades brasileiras
▪ cidade, população
▪ Belo Horizonte, 2521564
▪ Campinas, 1213792
▪ Campo Grande, 906092
▪ Curitiba, 1948626
▪ Dourados, 225495
▪ Florianópolis, 508826
▪ Fortaleza, 2686612
▪ Piracicaba, 407252
▪ Ponta Porã, 93937
▪ Porto Alegre, 1488252
▪ Rio de Janeiro, 6747815
▪ Salvador, 2886698 
▪ São Paulo, 12325232
◦ utilize a função carregar_arquivo_csv, do módulo util, para carregar o arquivo
PopulaçõesCidadesBrasileiras na lista populações_cidades_brasileiras
◦ itere na lista populações_cidades_brasileiras
▪ para obter a população da cidade_segurado
 retorno
◦ população
Joinvile Batista Junior - professor da Área de Computação da FACET/UFGD
Programação Aplicada à Engenharia - turma de Engenharia Mecânica - Lista de Execícios - 9/10
classe Segurado
 dados
◦ nome, cpf, estado_civil, sexo, data_nascimento, telefone, email, endereço
 métodos
◦ __init__, __str__
classe RiscoSeguro
 dados
◦ segurado, tempo_habilitação, tipo_residência, risco_seguro
◦ idade
▪ calculada com a função calcular_idade a partir da data de nascimento do segurado
◦ risco, categoria_risco
▪ calculados com a função calcular_risco_seguro
 métodos
◦ __init__, __str__
◦ e os seis métodos para representar os operadores relacionais
▪ comparando os valores de risco
Na função exercício5 do módulo main
 pule uma linha e imprima: Exercício 5
 crie a lista riscos_seguros com os objetos da classe RiscoSeguro
◦ utilize os dados de lista de riscos de seguros utilizados no exercício 4, acrescentando os 
dados adicionais listados a seguir
 itere na lista riscos_seguros e imprima os objetos da classe RiscoSeguro
 ordene a lista riscos_seguros aplicando a função sort(reverse=True) para ordenar os objetos 
da lista em ordem inversa
 itere na lista riscos_seguros ordenada e imprima os objetos da classe RiscoSeguro
    '''
def exercício4():
    '''
    Exercício 4
No diretório src crie o módulo seguro. No módulo seguro, implemente as funções descritas a seguir.
calcular_risco_seguro
 parâmetros
◦ idade, tempo_habilitação, tipo_residência, população_cidade
 funcionalidade
◦ calcular risco_seguro acrescentanco as seguintes pontuações 
▪ se idade
 entre 18 e 21 : 3 pontos
 entre 22 e 26 : 1 ponto
 entre 80 e 90 : 2 pontos
 acima de 90 : 4 pontos
▪ se tempo_habilitação
 menor que 1 ano : 2 pontos
▪ se população_cidade
 menor que 100 mil
◦ se tipo_residência
 casa : 1 ponto
 de 100 mil a 400 mil
◦ se tipo_residência
 casa : 2 pontos
 apto : 1 ponto
 mais de 400 mil a 1 milhão
◦ se tipo_residência
 casa : 3 pontos
 apartamento : 2 pontos
 mais de 1 milhão a 3 milhões
◦ se tipo_residência
 casa : 5 pontos
 apartamento : 2 pontos
 condomínio fechado : 1 ponto
 acima de 3 milhões
◦ se tipo_residência
 casa : 7 pontos
 apartamento : 3 pontos
 condomínio fechado : 2 ponto
◦ calcular categoria_risco da seguinte forma
▪ se risco_seguro
 menor que 5 : categoria_risco é baixa
 para risco entre 5 e 10 : categoria_risco é média
 maior que 10 : categoria_risco é alta
 retornar : risco_seguro, categoria_risco
Joinvile Batista Junior - professor da Área de Computação da FACET/UFGD
Programação Aplicada à Engenharia - turma de Engenharia Mecânica - Lista de Execícios - 7/10
imprimir_risco_seguro
 parâmetros
◦ nome, idade, tempo_habilitação, tipo_residência, população_cidade
 funcionalidade
◦ imprimir linha 1 e linha 2 da seguinte forma
▪ linha 1
 <nome> : com <idade> anos de idade, <tempo_habilitação> anos de habilitação, 
reside em <tipo_residência>, em uma cidade com cerca de <população_cidade>
habitantes
▪ linha 2:
 -- risco de seguro : <risco_seguro> -- categoria do seguro : <categoria_seguro>
◦ para calcular risco_seguro e categoria_seguro : utilizar a função calcular_risco_seguro
Na função exercício4 do módulo main
 pule uma linha e imprima: Exercício 4
 crie o dicionário riscos_seguros com chave nome composto de 6 dicionários de risco de
seguro com as seguintes chaves e valores
◦ nome, idade, tempo_habilitação, tipo_residência, população_cidade
▪ Marina Tempra, 22, 4, casa, 93937
▪ Leonardo Talure, 35, 17, apartamento, 2521564
▪ Adriana Raski, 18, 0, condomínio,12325232
▪ Fabrício Salvi, 85, 5, apartamento, 508826
▪ Alexia Caltaro, 87, 0, casa, 2886698
▪ Tales Petrus, 91, 70, casa, 12325232
 utilize as funções calcular_risco_seguro e imprimir_dados_risco_segurados para imprimir os
dados dos riscos de seguros do dicionário riscos_seguros
Joinvile Batista Junior - professor da Área de Computação da FACET/UFG
    '''
    pass
def exercício3():
    """
    Exercício 3
diagonal da matriz (em azul) -- matriz triangular superior -- matriz triangular inferior 
 1 7 3 7 2   1 7 3 7 2   1 0 0 0 0
 9 2 4 1 6   0 2 4 1 6   9 2 0 0 0
 4 8 2 3 5   0 0 2 3 5   4 8 2 0 0
 8 3 5 1 7   0 0 0 1 7   8 3 5 1 0
 4 6 1 5 9   0 0 0 0 9   4 6 1 5 9
No diretório src crie o módulo matriz. No módulo matriz, implemente as funções descritas a seguir.
gerar_diagonal_matriz
 parâmetros
◦ matriz_quadrada
 funcionalidade
◦ obter a dimensão da matriz
▪ matriz quadrada tem o mesmo número de linhas e de colunas
◦ preencha a lista diagonal com os valores da matriz correspondentes à diagonal da matriz
(valores da matriz com os mesmos índices na linha e na coluna)
▪ varie os índices da matriz de 0 até dimensão - 1 para obter os índices de linha ou
coluna correspondentes aos índices da diagonal das matriz
 retorno
◦ diagonal
gerar_matriz_triangular
 parâmetros
◦ matriz_quadrada
◦ tipo_matriz_triangular : superior ou inferior
 funcionalidade
◦ itere nas linhas matriz_quadrada
▪ itere nas colunas da matriz_quadrada
 copie para matriz_triangular os valores da linha da matriz
◦ se tipo_matriz_triangular : superior
▪ substituindo por 0 os valores com índices das colunas inferiores ao índice
da coluna da diagonal
◦ se tipo_matriz_triangular : inferior
▪ substituindo por 0 os valores com índices das colunas superiores ao
índice da coluna da diagonal
 retorno
◦ matriz_triangular
Na função exercício3, do módulo main, implemente:
 pule uma linha e imprima: Exercício 3
 inicialize matriz_quadrada com os dados da matriz ilustrada acima
 utilize a função gerar_diagonal_matriz para imprimir a diagonal da matriz_quadrada
 utilize a função gerar_matriz_triangular para imprimir a matriz triangular superior e a matriz
triangular inferior da matriz_quadrada
Joinvile Batista Junior - professor da Área de Computação da FACET/UFGD

    """
    pass

def exercício2():
    retangulo_objeto = retangulo(centro=(3,5), largura=2, comprimento=4)
    circulo_objeto = circulo(centro=(10, 13), raio=3)
    # b = a.calcular_perimetro()
    print(retangulo_objeto.calcular_area())
    print(retangulo_objeto.calcular_perimetro())
    print(circulo_objeto.calcular_perimetro())
    print(circulo_objeto.calcular_perimetro())



def exercício1():
    # Exercício 1
    alunos = 'Silvia Lemos da Silva, Fernando Tavares de Almeida, Rafael Souza Junior, Sandra Maria dos Santos, Pedro Valente Neto'
        
    emails_academicos = criar_emails_acadamicos(alunos=alunos)
    for x in emails_academicos:
        print(x)

if __name__ == '__main__':
    exercício1()
    exercício2()
    exercício3()
    exercício4()
    exercício5()



