"""
Modulo Collections (Modulo conhecido por alta performance) - Ordered Dict


> Um dicionario que tem a ordem de inserção garantida

# Demonstrando Diferença entre Dict e Ordered Dict

from collections import OrderedDict

dict1 = {'a':1,'b':2}
dict2 = {'b':2,'a':1}
print(dict1 == dict2)
# True

odict1 = OrderedDict({'a':1,'b':2})
odict2 = OrderedDict({'b':2,'a':1})

print(odict1 == odict2)
# False


# Ordered dict retornou falso pois os elementos não são iguais pela ordem
"""



