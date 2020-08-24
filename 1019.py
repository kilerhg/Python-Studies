'''

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
Entrada

O arquivo de entrada contém um valor inteiro N.
Saída

Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

'''

segundos = (int(input()))
minutos = 0
hora = 0
while (segundos > 59) :
    segundos = segundos - 60   
    minutos = minutos + 1

while (minutos > 59) :
    minutos = minutos - 60   
    hora = hora + 1
    


print('%s:%s:%s' % (hora,minutos,segundos))

