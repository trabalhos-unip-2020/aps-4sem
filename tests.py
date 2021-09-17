#code
import random
from sorting import bubble_sort, merge_sort

any_numbers = random.sample(range(1, 100000), 100000)

if __name__ == '__main__':
    test_cases = {'Random numbers': any_numbers}

    print('>>>---<<< >>>---<<< >>>---<<< >>>---<<< >>>---<<<')

    for name, lista in test_cases.items():
        print('\nCaso de teste: {}'.format(name))
        print(lista)
        quicksort(lista)
        print('\nOrdenado:')
        print(lista)
    print('>>>---<<< >>>---<<< >>>---<<< >>>---<<< >>>---<<<')
