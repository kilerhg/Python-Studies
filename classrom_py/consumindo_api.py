


var_python = '''
https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda={moeda}&@dataInicial={data_inicial}&@dataFinalCotacao={data_final}
'''.format(moeda='USD', data_inicial='01/01/2019', data_final='01/01/2020')

print(var_python)

# 

'''
Metodos HTTP:

GET: Buscar informacoes
POST: Criar informacoes
PUT: Alterar informacoes
DELETE: Deletar informacoes

'''