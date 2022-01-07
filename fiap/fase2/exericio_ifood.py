"""
Exercicio Ifood Fiap
desafio da sua equipe será a criação de um ranking dos restaurantes próximo ao endereço de entrega, por 
meio dos critérios de avaliação do restaurante e a menor distância. 
"""

# data_input = '''O Mineiro - nota 4.2 - distância 1.7 km / Amor aos Pedaços - nota 4.3 - distância 1.2 / We Coffe - nota 4.5 - distância 0.8 km
# Lamen Kazu - nota 4.8 - distância 0.7 km / Mr. Pretzels - nota 4.7 - distância 1,1 km / Brigaderia - nota 4.7 - distância 1.2 km'''

sample_input = [['o Mineiro', 4.2, 1.7], ['Amor aos Pedaços', 4.3, 1.2], ['We Coffe', 4.5, 0.8], ['amen Kazu', 4.8, 0.7], ['Mr. Pretzels', 4.7, 1.1], ['Brigaderia', 4.7 , 1.2]]

numero_restaurantes = 6
lista_restaurantes = []
lista_ordenada = []

# numero_restaurantes = int(input('Informe a quantidade de restaurantes desejada: '))

for restaurante in range(0, numero_restaurantes):
    nome = sample_input[restaurante][0] # Recebe nome Input
    nota = sample_input[restaurante][1] # Recebe nota
    distancia = sample_input[restaurante][2] # Recebe 
    # nome = str(input('Nome Restaurante: ')) # Recebe nome Input
    # nota = float(input('Nota Restaurante: ')) # Recebe nota
    # distancia = float(input('Distancia Restaurante (em km): ')) # Recebe 
    restaurante = [nome, nota, distancia, nota + (100 - distancia) / 1000] # Atribui elementos para uma lista e calcula nota Com fator de distancia
    lista_restaurantes.append(restaurante) # Adiciona lista com elementos restaurantes na lista total

while len(lista_restaurantes) != 0: # Itera lista total enquanto lista_restaurantes for diferente de 0
    maior_nota = 0 # Atribui um valor inicial
    restaurante_maior_nota = None  # Atribui um valor inicial
    for restaurante in lista_restaurantes: # Itera restaurante por restaurante
        if restaurante[3] > maior_nota: # Valida se nota com fator de distancia é a maior
            maior_nota = restaurante[3] 
            restaurante_maior_nota = restaurante
    lista_ordenada.append(restaurante_maior_nota) # Adiciona na ordem
    lista_restaurantes.remove(restaurante_maior_nota) # Remove da origem

# print('-'*10+' Restaurante '+'-'*10) # Método Antigo
print(f'{" Restaurantes ":-^25}')

cont = 0
for restaurante in lista_ordenada:
    cont += 1
    print()

    print(f'Posição: {cont}\nNome: {restaurante[0]}\nNota: {restaurante[1]}\nDistancia: {restaurante[2]} KM')

print(lista_ordenada)