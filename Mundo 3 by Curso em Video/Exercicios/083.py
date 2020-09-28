# digite uma expressao qualquer que use parenteses, devera analisar se os parenteses estão abertos e fechados na ordem correta
valor = str(input('Digite uma Expressão:')).strip()
listaa = []
listaf = []
ct = 0
for pos, x in enumerate(valor):
    if x == '(':
        listaa.append(pos)
    elif x == ')':
        listaf.append(pos)
if '(' in valor and ')' in valor:
    if valor.count('(') == valor.count(')'):
        qtd = valor.count('(')
        for x in range(0,len(listaa)):
            if listaa[x] < listaf[x]:
                ct += 1
        if ct == qtd:
            print('A expressão está correta!!')
        else:
            print('A expressão está incorreta!! Ela abre e fecha o mesmo numero de parenteses, porem um ou mais está na direção errada')
    else:
        print('A expressão está incorreta!! o Numero de parenteses abertos e fechados são diferentes')
else:
    print('A expressão não tem parenteses')

print('Fim....')
