# Instalando Bibliotecas
# pip install pillow

# Importando Bibliotecas
from PIL import Image
import os



# Lendo Todos Os Arquivos Na Pasta
origem = './jpg/'
for raiz, diretorios, files in os.walk(origem):
    arquivos = files

destino = './webp/'
for arquivo in arquivos:
    image = Image.open(f'{origem}{arquivo}')
    image.save(f'{destino}{arquivo[:-4]}.webp')