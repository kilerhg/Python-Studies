import re

# Sempre utilizar regex em string com r''. assim evitando repetir caracteres de escape

## Metódos de utilização

### findall() -> Encontra todas as ocorrências e retorna uma lista
### search() -> Encontra o Primeiro e Retorna um objeto Match
### sub() -> Substitui as ocorrências encontradas. podendo limitar a um ou todos.
### compile() -> Cria um objeto compilado que pode ser utilizado varias vezes sem reprocessamento em memoria


regex_script = r'[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}'
text = 'asdsadasdasdas 123.123.123-12 asadasdsads'

print(re.search(regex_script, text)) # Retorna um Objeto Match com posição e conteudo
print(re.findall(regex_script, text)) # Retorna lista de todas ocorrencias
print(re.sub(regex_script, 'au', text)) # Retorna o script original com substituição
