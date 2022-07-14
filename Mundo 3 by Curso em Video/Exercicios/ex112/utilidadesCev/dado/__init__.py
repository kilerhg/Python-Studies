def leiaDinheiro(texto='Digite um Valor:'):
    while True:
        r = input(texto).strip()
        if r.count(',') > 0:
            r = r.replace(',','.')
        if r.replace('.','',1).isdecimal():
            r = float(r)
            break
        print(f'O valor "{r}" não é um numero!!')
    return r