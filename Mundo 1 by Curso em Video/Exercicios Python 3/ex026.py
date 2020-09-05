# leia uma frase, vezes aparece a letra A, a primeira posição ela apareçe pela primeira vez, e a posiçao ultima vez
frase = str(input('Digite uma frase:')).strip()
print(f' Quantas Vezes aparece a letra A: {frase.upper().count("A")}\n A primeira vez que aparece a letra A : {frase.upper().find("A")+1}\n A ultima vez que aparece : {frase.upper().rfind("A")+1}')