'''
Escrevendo um iterador customizado 
'''




class contador:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            x = self.start
            self.start += 1
            return x
        raise StopIteration


objeto_contador = contador(1, 10)
# it = iter(objeto_contador)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for x in contador(1, 10):
    print(x)