from random import randint

def bubble_sort(array):
    sorting_array = array[:]
    number_items = len(sorting_array)
    all_sorted = False
    while not all_sorted:
        print()
        all_valid = []
        for pos in range(number_items):
            if pos+1 < number_items: # fazendo validação para não buscar um elemento que não existe (Index error)
                print(f"comparando: {sorting_array[pos]} > {sorting_array[pos+1]} - {sorting_array[pos] > sorting_array[pos+1]}")
                if sorting_array[pos] > sorting_array[pos+1]:
                    print(sorting_array)
                    sorting_array[pos], sorting_array[pos+1] = sorting_array[pos+1], sorting_array[pos] # Invertendo o numero caso seja maior
                    all_valid.append(False)
                else:
                    all_valid.append(True)
        all_sorted = all(all_valid) # Verificando se nessa iteração nenhuma alteração foi feita
    return sorting_array

array_unsorted = [1, 7, 3, 2, 4, 6, 5, 8, 9, 10]

print(array_unsorted)
print()

sorted_array = bubble_sort(array_unsorted)

print(sorted_array)
