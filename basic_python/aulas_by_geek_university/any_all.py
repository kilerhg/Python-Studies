'''
Any & All

All() -> Retorna True se todos os elementos do iterável são verdadeiros ou se o iterável está vazio
any() -> Retorna True se qualquer Elemento do iterável for verdadeiro, se o iterável estiver vazio, retorna False

# OBS: Segundo all() listas vazia: [] é True, porém segundo bool é False
import string



# Praticando

comprehension_01 = [num for num in range(20) if num % 2 == 0]
comprehension_02 = [num for num in range(20) if num % 2 == 1]
comprehension_03 = [num*100 for num in range(20) if num % 2 == 1]
comprehension_04 = [num*-1 for num in range(20) if num % 2 == 1]
comprehension_05 = [letter for letter in string.ascii_letters if letter != 'a']
comprehension_06 = []



print(all(comprehension_01)) # False Pois O elemento 0 é considera Falso
print(all(comprehension_02)) # True Pois todos são verdadeiros
print(all(comprehension_03)) # True Pois todos são verdadeiros
print(all(comprehension_04)) # True Pois todos são verdadeiros
print(all(comprehension_05)) # True Pois todos são verdadeiros
print(all(comprehension_06)) # True Pois todos são verdadeiros
print(bool(comprehension_06)) # False pois a lista é vazia * UTILIZANDO BOOL


print('0')
print(any(comprehension_01)) # True Pois algum elemento é verdadeiro
print(any(comprehension_02)) # True Pois algum elemento é verdadeiro
print(any(comprehension_03)) # True Pois algum elemento é verdadeiro
print(any(comprehension_04)) # True Pois algum elemento é verdadeiro
print(any(comprehension_05)) # True Pois algum elemento é verdadeiro
print(any(comprehension_06)) # False pois a lista é vazia
print(bool(comprehension_06)) # # False pois a lista é vazia * UTILIZANDO BOOL
'''





