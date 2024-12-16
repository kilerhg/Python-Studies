array_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
array = array_original[:]

def binary_search(number_to_find, array):
    
    number_elements = len(array)
    
    current_number = 0
    steps = 0

    print(array_original)
    print(f'Numero a ser encontrado: {number_to_find}')
    
    while current_number != number_to_find:
        print(steps)
        steps += 1
        print(array)
        position = number_elements//2
        guess = array[position]
        if guess > number_to_find:
            array = array[:position]
            number_elements = len(array)
            print(f'chute é maior: {guess}')

        elif guess < number_to_find:
            array = array[position:]
            number_elements = len(array)
            print(f'chute é menor: {guess}')
        else:
            print(f'acertou: {guess}')
            current_number = guess

number_to_find = 5

binary_search(number_to_find, array)