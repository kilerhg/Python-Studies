'''

Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados.
A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

    se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
    se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

Entrada

A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).
Saída

Imprima todas as classificações do triângulo especificado na entrada.

'''

linha = input().split(' ')
linha = list(map(float,linha))
linha.sort()
C,B,A = linha

if A < (B+C) :
    if A ** 2 == B ** 2 + C ** 2 :
        print('TRIANGULO RETANGULO')
    if A ** 2 > B ** 2 + C ** 2 :
        print('TRIANGULO OBTUSANGULO') 
    if A ** 2 < B ** 2 + C ** 2 :
        print('TRIANGULO ACUTANGULO')    
    if A == B == C :
        print('TRIANGULO EQUILATERO') 
    if ((A == B) or (B == C)) and (A != C) :
        print('TRIANGULO ISOSCELES')
else :
    print('NAO FORMA TRIANGULO')
