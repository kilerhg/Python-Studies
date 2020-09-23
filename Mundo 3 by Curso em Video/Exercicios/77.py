# tupla com varias palavras, e mostrar quais verbos está dentro de cada um.

palavras = ('palavras','mostrar','verbos','dentro','cada','melhores','nacional','codigo','escrever','jogar','divertir','python','ler','nascer')
for c in range(0,len(palavras)):
    print(f' As vogais da palavra {palavras[c]: <10} São : ',end=' ')
    for x in palavras[c]:
        if x in 'aeiou':
            print(x, end=' ')
    print('')
