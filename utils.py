from math import exp


def get_normal(a, b):
    return lambda x: exp(-((x - a) ** 2) / (2 * b ** 2))


def print_indexes_list(label: str, name_list: [str]):
    print()
    print(label)
    for index, name in enumerate(name_list, start=1):
        print(f'{index}. {name}')
