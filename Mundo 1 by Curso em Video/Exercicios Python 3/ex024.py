# leia uma cidade e verifique se começe com a palavra "SANTO"

cidade = input('Digite o nome de uma cidade:').strip()
print(f' A começa com Santo: {"SANTO" in cidade.upper()[0:5]}')