# Melhore o desafio 61 pedindo para o usuario quantos termos a mais ele quer mostrar

pt = int(input('Digite o valor do primeiro Termo:'))
ra = int(input('Digite o valor da Razão:'))
nt = 1
rt = pt
pa = 11
ntt = nt
while pa != 0:
    nt = 0
    print('= =' * 30)
    while nt != pa:
        print(f' O termo N-{ntt:2} é igual á {rt:3}')
        rt += ra
        nt += 1
        ntt += 1
    pa = int(input('Você gostaria de continuar? Se sim Digite a quantidade de Termos para continuarmos, caso não digite [0]:'))
print('Fim')