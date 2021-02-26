import os

steam = '66054934'
link = f'https://steamidfinder.com/lookup/[U%3A1%3A{steam}]/'
path = "C:/Program Files (x86)/Steam/userdata"
cfg = f'{path}/{steam}/730/local/cfg/config.cfg'
pastas = []

for raiz, diretorios, arquivos in os.walk(path):
	if len(diretorios) != 0:
			pastas.append(diretorios)

pastas = pastas[0]

for pospasta, pasta in enumerate(pastas):
	if pasta.isnumeric():
		pass
	else:
		pastas.pop(pospasta)



print(pastas)
print(link)
print(cfg)