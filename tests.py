#code
import contextlib
import random
import time


from sorting import bubble_sort

@contextlib.contextmanager
def timeit(name):
    start = time.time()
    yield
    end = time.time()
    took = end - start
    print(f"The {name} took {took:.4f}s")

any_numbers = random.sample(range(1, 100000), 100000)

if __name__ == '__main__':
    test_cases = {'Random numbers': any_numbers}

    print('>>>---<<< >>>---<<< >>>---<<< >>>---<<< >>>---<<<')

    for name, lista in test_cases.items():
        print('\nCaso de teste: {}'.format(name))
        print(lista)
        bubble_sort(lista)
        print('\nOrdenado:')
        print(lista)
    print('>>>---<<< >>>---<<< >>>---<<< >>>---<<< >>>---<<<')
