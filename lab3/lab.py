from lab3.criteria import *
from lab3.fuzzyficator import SingletonFuzzyficator

xs = [9, 2.5, 8, 5, 5]

print(f'Входные данные {", ".join([f"x{index + 1}={x}" for index, x in enumerate(xs)])}')
print()
print('1 Уровень - фаззификация')
As = [
    SingletonFuzzyficator(criteria).fuzzy(x)
    for x, criteria in zip(
        xs,
        [A1(), A2(), A3(), A4(), A5()]
    )
]
