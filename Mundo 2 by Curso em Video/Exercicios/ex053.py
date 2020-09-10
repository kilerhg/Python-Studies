# leia uma frase e verifique se ela é um palindromo, descosiderando os espaços

f = str(input('Digite uma frase:')).strip()
f = f.split()
f = ''.join(f)
f = f.upper()
sm = 0
for x in range(1,len(f)+1):
    xx = (len(f)+1) - x
    # print(f[x-1],f[xx-1])
    if f[x-1] == f[xx-1]:
        sm += 1
    print(f[x-1],f[xx-1])
if sm == len(f):
    print('Está frase é um Palindromo')
else:
    print('Está frase não é um Palindromo')