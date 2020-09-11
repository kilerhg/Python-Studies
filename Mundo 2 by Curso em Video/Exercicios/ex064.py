# Leia varios numeros inteiros so parar quando digitar 999, no final mostre quantos numeros foram digitados e qual foi a soma entre eles desconsiderando o flag
cn = 0
n = 0
ct = 0
while cn != 999:
    cn = int(input('Digite um numero Inteiro[para parar digite 999]:'))
    if cn != 999:
        n += cn
        ct +=1
print(f' A soma resultou: {n} com {ct} numeros')