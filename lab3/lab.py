from lab3.criteria import *
from lab3.fuzzyficator import SingletonFuzzyficator
from lab3.pred_activations import C1, PreadActivationProcess, C2

# Настройки
Fuzzyficator = SingletonFuzzyficator
implication = lambda x, y: min(1, 1 - x + y)

xs = [9, 2.5, 8, 5, 5]

print(f'Входные данные {", ".join([f"x{index + 1}={x}" for index, x in enumerate(xs)])}')
print()
print('1 Уровень - фаззификация')
As = [
    Fuzzyficator(criteria).fuzzy(x)
    for x, criteria in zip(
        xs,
        [A1(), A2(), A3(), A4(), A5()]
    )
]

print()
print('2 Уровень – активация (подусловия)')
# TODO Описать все подусловия
Cs = [
    C1(As[0], implication),
    C2(As[3], implication)
]
processor = PreadActivationProcess(Cs)
result_Cs = processor.process()
