from math import exp
from tabulate import tabulate


def get_normal(a, b):
    return lambda x: exp(-((x - a) ** 2) / (2 * b ** 2))


def print_indexes_list(label: str, name_list: [str]):
    print()
    print(label)
    for index, name in enumerate(name_list, start=1):
        print(f'{index}. {name}')


def print_table(table, header, title: str = ''):
    if title:
        print()
        print(title)
    print(tabulate(
        table,
        headers=header
    ))


def max_norm_vector(vector) -> [float]:
    maximum = max(vector)
    return [
        el / maximum
        for el in vector
    ]


def norm_vector(vector) -> [float]:
    summary = sum(vector)
    return [
        el / summary
        for el in vector
    ]


def get_interval(range, step):
    start, stop = range
    position = start

    while position <= stop:
        yield position
        position += step
