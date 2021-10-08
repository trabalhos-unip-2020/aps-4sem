import contextlib
import random
import time

from sorting import (
    bubble_sort,
    merge_sort,
)


@contextlib.contextmanager
def timeit(name):
    start = time.time()
    yield
    end = time.time()
    took = end - start
    print(f"O {name} levou {took:.4f}s")


def nearly_sorted_array(size):
    array = [i for i in range(0, size + 1)]

    for i in range(10, size, 10):
        array[i], array[i - 1] = array[i - 1], array[i]

    return array


if __name__ == '__main__':
    number_of_items = 1000000

    normal_array = [random.randint(0, number_of_items)
                    for i in range(number_of_items)]
    random.shuffle(normal_array)

    nearly_sorted = nearly_sorted_array(number_of_items)
    reversed_array = sorted(normal_array, reverse=True)
    sorted_array = sorted(normal_array)

    algorithms = {
        "bubble_sort": bubble_sort.sort,
        "merge_sort": merge_sort.sort,
    }

    print("Ordenando Array aleatorio")
    print("-" * 50)
    for name, sort in algorithms.items():
        copy_array = list(normal_array)

        with timeit(name):
            sort(copy_array)

        assert copy_array == sorted(normal_array)

    print("\n\nClassificando a matriz quase classificada")
    print("-" * 50)
    for name, sort in algorithms.items():
        copy_array = list(nearly_sorted)

        with timeit(name):
            sort(copy_array)

        assert copy_array == sorted(nearly_sorted)

    print("\n\nClassificando a matriz classificada invertida")
    print("-" * 50)
    for name, sort in algorithms.items():
        copy_array = list(reversed_array)

        with timeit(name):
            sort(copy_array)

        assert copy_array == sorted(reversed_array)